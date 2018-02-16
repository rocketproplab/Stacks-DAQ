#!/usr/bin/python

import subinitial.stacks as stacks

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

core.rgbled.set(int("0xFF00FF04",16))

analogdeck.rgbled.set(int("0xFF00FF04",16))
