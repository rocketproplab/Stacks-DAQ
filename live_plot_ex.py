#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# import numpy.random
import math
import random


fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(nrows=1, ncols=2)

left_gs =  gridspec.GridSpecFromSubplotSpec(nrows=3, ncols=1, subplot_spec=gs[0])
right_gs = gridspec.GridSpecFromSubplotSpec(nrows=2, ncols=1, subplot_spec=gs[1])

ax = []

ax.append(fig.add_subplot(left_gs[0,0]))
ax.append(fig.add_subplot(left_gs[1,0]))
ax.append(fig.add_subplot(left_gs[2,0]))
ax.append(fig.add_subplot(right_gs[0,:]))
# ax.append(fig.add_subplot(right_gs[1,]))


# gs.set_title('Test Stand Static Fire')
ax[0].set_title('Load Cell #1')
ax[1].set_title('Load Cell #2')
ax[2].set_title('Load Cell #3')

ax[3].set_title('Total Load')

plt.show()

samples = []
sample_count = 0
while(True):

    x  = random.gauss((math.sin(sample_count)) ** 2,0.1)
    samples.append(x)
    ax[0].plot(sample_count , samples, 'r--')

    sample_count += 1
    if(sample_count > 500000):
        samples.pop()

    plt.show()
