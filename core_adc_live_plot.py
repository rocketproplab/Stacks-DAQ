#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

import subinitial.stacks as stacks
import time
import math
import csv
import numpy as np
import random

core = stacks.Core(host="192.168.2.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

dmm = analogdeck.dmm

## Used for the actual load cell data calculation
NUM_LOAD_CELLS = 3
EXCITATION_VOLTAGE = 12 # Volts
SAMPLE_TIME = 5.0 # Seconds
WAVE_GEN_SAMPLES = 100
RATED_OUTPUT = 2 # mV/V
LOAD_CELL_SCALE = RATED_OUTPUT * EXCITATION_VOLTAGE # mV
LOAD_CELL_FORCE = 1000 #lbf, pound force

# Startup sequence
for i in range(16,127):

    core.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
    analogdeck.rgbled.set(int(("0x00FF00" + hex(i)[2:]), 16))
# End of "startup" sequence

# Load the csv file
csv_file = open('output_data/core_adc_load_cell_test_num.csv', "w")
csv_writer = csv.writer(csv_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL)

# Enables the ADC's on the core of the Stacks
core.adc.enable(0,1,2,3)

count = 0
csv_row = []
voltage_samples = []
force_reading = []
for i in range(NUM_LOAD_CELLS):
    csv_row.append([])
    force_reading.append(0)

start = time.time()

while (time.time() - start) < SAMPLE_TIME:
    # Gets the voltages of all the DMMs on the stacks
    voltage_sample = core.adc.get_all()

    csv_row.clear()
    for i in range(NUM_LOAD_CELLS):
        # Calculates the force on each of load cells
        force_reading[i] = voltage_sample[i] * (LOAD_CELL_FORCE / LOAD_CELL_SCALE) * 1000
        ''' Coverts the voltage reading of the load cell to a pount force
            force reading (lbf) = [Sample (V)]
                                * [LOAD_CELL_FORCE (lbf) / LOAD_CELL_SCALE (mv)]
                                * [1000 (mv/V)]
        '''
        # Prints data to a csv file

        csv_row += [i,(time.time() - start), voltage_sample[i], force_reading[i]]
        # Prints data to the console
        print("Load cell : {},sample time: {}s, measurement: {} V, force: {} lbf".format(i, time.time() - start, voltage_sample[i], force_reading[i]))

        # print(csv_row)
    csv_writer.writerow(csv_row)

    count +=1






t = np.arange(0.0, 5, 0.01)
s1 = 200*np.sin(1 * np.pi * t) + 200
s2 = 200*np.exp(-t)*np.sin(3* np.pi * t) + 250
s3 = 200*np.sin(2 * np.pi * t)+225
s4 = np.add(np.add(s1, s2), s3)

# samples =
#
#
#

# sample_time = []
samples = dict()



def animate(i):

    # First bracket is to get to the samples
    for i in range(NUM_LOAD_CELLS):
        samples[i].clear()
        samples[i].plot(samples)


ani = animation.FuncAnimation(fig, animate, interval=25)#

# plt.ion()
fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(nrows=1, ncols=2)

left_gs =  gridspec.GridSpecFromSubplotSpec(nrows=3, ncols=1, subplot_spec=gs[0])
right_gs = gridspec.GridSpecFromSubplotSpec(nrows=2, ncols=1, subplot_spec=gs[1])

ax = []

ax.append(fig.add_subplot(left_gs[0,0]))
ax.append(fig.add_subplot(left_gs[1,0], sharex=ax[0]))
ax.append(fig.add_subplot(left_gs[2,0], sharex=ax[0]))
ax.append(fig.add_subplot(right_gs[0,:], sharex=ax[0]))
# ax.append(fig.add_subplot(right_gs[1,]))


fig.suptitle('Test Stand Static Fire')

ax[3].set_title('Total Load')
ax[0].set_title('Load Cell #1')
ax[1].set_title('Load Cell #2')
ax[2].set_title('Load Cell #3')


ax[0].set_ylim(0,500)
ax[1].set_ylim(0,500)
ax[2].set_ylim(0,500)
ax[3].set_ylim(0,1200)

ax[0].plot(t, s1)
ax[1].plot(t, s2)
ax[2].plot(t, s3)
ax[3].plot(t, s4)

# print(type(ax[0]))



plt.show()

#
# samples = []
# sample_count = 1
# while(True):
#
#     x  = 500 * random.gauss(((math.sin(sample_count)) ** 2) / 2, 1.1)
#     samples.append(x)
#     ax[0].plot(samples)
#
#     sample_count += 0.001
#     if(sample_count > 50):
#         samples.pop()
#
#     plt.show()
#     plt.pause(0.00001)
#     fig.draw()


samples_per_sec = count / SAMPLE_TIME
print("Samples: {}, Elapsed Time: {}s, Samples per Second {} Hz".format(count, SAMPLE_TIME, samples_per_sec))
csv_file.close()

for i in range(16,127):

    core.rgbled.set(int(("0xFF00FF" + hex(i)[2:]), 16))
    analogdeck.rgbled.set(int(("0xFF00FF" + hex(i)[2:]), 16))
    time.sleep(3/1000)
# End of "startup" sequence
