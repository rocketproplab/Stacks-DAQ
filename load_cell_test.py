#!/usr/bin/python

import subinitial.stacks as stacks

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

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


# Set up ADC
