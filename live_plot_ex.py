#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



layout = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(ncols=3, nrows=2)

ax = []

ax.append(plt.subplot(gs[0,0]))
ax.append(plt.subplot(gs[0,1]))
ax.append(plt.subplot(gs[0,2:]))
ax.append(plt.subplot(gs[1,0:2]))
ax.append(plt.subplot(gs[1, -1]))



plt.show()
