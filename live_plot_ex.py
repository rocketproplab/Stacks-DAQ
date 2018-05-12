#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation


# import numpy.random
import math
import numpy as np
import random

NUM_LOAD_CELLS = 3

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
