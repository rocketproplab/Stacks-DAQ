#!/usr/bin/python

import subinitial.stacks as stacks
from time import sleep

core = stacks.Core(host="192.168.1.49")

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


for i in reversed(range(5,10)):
    for j in range(0,10):
        for k in range(0,4):
            analogdeck.solenoiddrivers.engage(0)

        sleep(2 ** i / 1000)

        for k in range(0,4):
            analogdeck.solenoiddrivers.disengage(0)

        sleep(2 ** i / 1000)
