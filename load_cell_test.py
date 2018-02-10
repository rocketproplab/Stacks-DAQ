#!/usr/bin/python

import subinitial.stacks as stacks
import time
import math
import csv

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

dmm = analogdeck.dmm

# Used for that totally sick LED startup sequence
LED_ITER = 255

## Used for the actual load cell data calculation
NUM_LOAD_CELLS = 3
EXCITATION_VOLTAGE = 12 # Volts
SAMPLE_TIME = 60.0 # Seconds
WAVE_GEN_SAMPLES = 10
RATED_OUTPUT = 2 # mV/V
LOAD_CELL_SCALE = RATED_OUTPUT * EXCITATION_VOLTAGE # mV
LOAD_CELL_FORCE = 1000 #lbf, pound force

# Change leds for no real reason except it will look like its doing something
# really important
for i in range(0,2):
    for j in range(LED_ITER):

        core.rgbled.set(int(("00FF00FF" + "{:02x}".format(round(math.sin(j/ LED_ITER * math.pi) * 255))), 16))
        analogdeck.rgbled.set(int(("0xFF00FF" + "{:02x}".format(round(math.sin(j/ LED_ITER * math.pi) * 255))), 16))
        time.sleep(5 / 10000)

for i in range(16,127):

    core.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
    analogdeck.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
# End of "startup" sequence



# Set the voltage of the something

sine_samples = []
for i in range(WAVE_GEN_SAMPLES):
    sine_samples.append(2 * (math.sin( 2 * math.pi * i/ WAVE_GEN_SAMPLES)))

analogdeck.wavegen.update_waveform(samplerate_hz=500, samples=sine_samples)
analogdeck.wavegen.set_control(analogdeck.wavegen.MODE_WAVEFREERUN)


# Set excitation voltage to +12V as the max on the load cell is +18V and the
# max voltage of the ADC input is +13V and the recommended is +2.5V

# analogdeck.sourcemeter.set_sourcevoltage(2.5)

# Load the csv file
csv_file = open('output_data/load_cell_test_num.csv', "w")
csv_writer = csv.writer(csv_file, delimiter='\n', quotechar='"', quoting=csv.QUOTE_ALL)

# Set up ADC
# dmm.set_channelranges(range0=dmm.RANGE_AUTO)
#
# dmm.stream_arm(channel=0, samplerate=dmm.SAMPLERATE_1200HZ, range_=dmm.RANGE_AUTO, timeout=10)
#
# dmm.stream_trigger()

dmm.freerun(mask=0b111, samplerate=dmm.SAMPLERATE_14400HZ)

# Initializes sample lists
num_samples = 0
voltage_samples = []
force_reading = []
for i in range(NUM_LOAD_CELLS):
    force_reading.append(0)

# Starts the timer
start = time.time()

while (time.time() - start) < SAMPLE_TIME:
        # Gets the voltages of all the DMMs on the stacks
        voltage_samples = dmm.get_results()

        # Calculates the force on each of load cells
        for i in range(NUM_LOAD_CELLS):
            force_reading[i] = voltage_samples[i] * (LOAD_CELL_FORCE / LOAD_CELL_SCALE) * 1000
            ''' Coverts the voltage reading of the load cell to a pount force
                force reading (lbf) = [Sample (V)]
                                    * [LOAD_CELL_FORCE (lbf) / LOAD_CELL_SCALE (mv)]
                                    * [1000 (mv/V)]
            '''
            # Prints data to a csv file
            csv_writer.writerow([i, (time.time() - start), voltage_samples[i], force_reading[i]])

            # Prints data to the console
            print("loadcell: {}, sample time: {}s, measurement: {} V, force: {} lbf".format(i, time.time() - start, voltage_samples[0], force_reading[0]))

        # for i in range(NUM_LOAD_CELLS):


csv_file.close()
