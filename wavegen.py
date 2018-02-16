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
WAVE_GEN_SAMPLES = 200
RATED_OUTPUT = 2 # mV/V
LOAD_CELL_SCALE = RATED_OUTPUT * EXCITATION_VOLTAGE # mV
LOAD_CELL_FORCE = 1000 #lbf, pound force


for i in range(16,127):

    core.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
    analogdeck.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
# End of "startup" sequence


sine_samples = []
for i in range(WAVE_GEN_SAMPLES):
    sine_samples.append(LOAD_CELL_SCALE/ 1000 * (math.sin(math.pi * i/ WAVE_GEN_SAMPLES)) ** 2)

analogdeck.wavegen.update_waveform(samplerate_hz=200, samples=sine_samples)
analogdeck.wavegen.set_control(analogdeck.wavegen.MODE_WAVEFREERUN)
