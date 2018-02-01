#!/usr/bin/python

import subinitial.stacks as stacks
import time

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

dmm = analogdeck.dmm

SAMPLE_TIME = 120 # Measured in seconds

# Change leds for no real reason except it will look like its doing something
# really important
for i in range(0,2):
    for j in range(16,255):

        core.rgbled.set(int(("0x00FF00" + hex(j)[2:]), 16))
        analogdeck.rgbled.set(int(("0x00FF00" + hex(j)[2:]), 16))
        sleep(1 / 1000)

    for j in reversed(range(16,255)):

        core.rgbled.set(int(("0x00FF00" + hex(j)[2:]), 16))
        analogdeck.rgbled.set(int(("0x00FF00" + hex(j)[2:]), 16))
        sleep(1 / 1000)

for i in range(16,127):

    core.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
    analogdeck.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
    sleep(1 / 1000)
# End of "startup" sequence



# Set the voltage of the something

# Set excitation voltage to +12V as the max on the load cell is +18V and the
# max voltage of the ADC input is +13V and the recommended is +2.5V
analogdeck.sourcemeter.set_sourcevoltage(2.5)

# Set up ADCanalogdeck.dmm.stop
dmm.set_channelranges(range0=dmm.RANGE_LOW_2V5)

dmm.stream_arm(channel=0, samplerate=dmm.SAMPLERATE_10HZ, range_=dmm.RANGE_MED_25V)

start = time.time()
dmm.trigger()

while (time.time() - start) < SAMPLE_TIME:
    for sample in dmm.stream():

        # Do something with sample
        print(sample)
