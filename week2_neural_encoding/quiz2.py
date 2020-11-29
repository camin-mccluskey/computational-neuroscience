"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from week2_neural_encoding.compute_sta import compute_sta


def run():

    FILENAME = 'c1p8.pickle'

    with open(FILENAME, 'rb') as f:
        data = pickle.load(f)

    stim = data['stim']
    rho = data['rho']

    # Fill in these values
    sampling_rate = 500 # 500Hz
    sampling_period = (1 / sampling_rate) * 1000 # in ms
    num_timesteps = 150 # num timesteps for 300ms preceding the spike

    sta = compute_sta(stim, rho, num_timesteps)

    time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

    plt.plot(time, sta)
    plt.xlabel('Time (ms)')
    plt.ylabel('Stimulus')
    plt.title('Spike-Triggered Average')

    plt.show()


if __name__ == '__main__':
    run()
