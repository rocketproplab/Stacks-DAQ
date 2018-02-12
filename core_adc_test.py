#!/usr/bin/python

import subinitial.stacks as stacks
import time
import math
import csv

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

dmm = analogdeck.dmm


## Used for the actual load cell data calculation
NUM_LOAD_CELLS = 3
EXCITATION_VOLTAGE = 12 # Volts
SAMPLE_TIME = 3.0 # Seconds
WAVE_GEN_SAMPLES = 100
RATED_OUTPUT = 2 # mV/V
LOAD_CELL_SCALE = RATED_OUTPUT * EXCITATION_VOLTAGE # mV
LOAD_CELL_FORCE = 1000 #lbf, pound force


for i in range(16,127):

    core.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
    analogdeck.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
# End of "startup" sequence



sine_samples = []
for i in range(WAVE_GEN_SAMPLES):
    sine_samples.append(LOAD_CELL_SCALE/ 1000 * (math.sin(math.pi * i/ WAVE_GEN_SAMPLES)) ** 8)

analogdeck.wavegen.update_waveform(samplerate_hz=60, samples=sine_samples)
analogdeck.wavegen.set_control(analogdeck.wavegen.MODE_WAVEFREERUN)


# Load the csv file
csv_file = open('output_data/load_cell_test_num.csv', "w")
csv_writer = csv.writer(csv_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)

core.adc.enable(0)

count = 0
start = time.time()

while (time.time() - start) < SAMPLE_TIME:
    # Gets the voltages of all the DMMs on the stacks
    voltage_sample = core.adc.get(0)

    # Calculates the force on each of load cells
    force_reading = voltage_sample * (LOAD_CELL_FORCE / LOAD_CELL_SCALE) * 1000
    ''' Coverts the voltage reading of the load cell to a pount force
        force reading (lbf) = [Sample (V)]
                            * [LOAD_CELL_FORCE (lbf) / LOAD_CELL_SCALE (mv)]
                            * [1000 (mv/V)]
    '''
    # Prints data to a csv file

    csv_row = [(time.time() - start), voltage_sample, force_reading]
    # Prints data to the console
    print("sample time: {}s, measurement: {} V, force: {} lbf".format(time.time() - start, voltage_sample, force_reading))

    # print(csv_row)
    csv_writer.writerow(csv_row)

    count +=1


samples_per_sec = count / SAMPLE_TIME
print("Samples: {}, Elapsed Time: {}s, Samples per Second {} Hz".format(count, SAMPLE_TIME, samples_per_sec))
csv_file.close()
