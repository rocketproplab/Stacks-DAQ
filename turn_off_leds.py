#!/usr/bin/python

import subinitial.stacks as stacks

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

core.rgbled.set(0)

analogdeck.rgbled.set(0)
