# (disk, platter, loc)
# FAT alternates disks every _ blocks

import numpy as np
import time
import threading


class Disk:

    def __init__(self, sched_alg, platters=2, blocks=1000):
        '''
        create a disk
        '''

        self.head_loc = 0       # head location
        self.schd = sched_alg   # select location
        self.n_plat = platters  # platters on each disk
        self.n_bloc = blocks    # blocks on each platter

        # array to hold 'data' of disc (None or a block reference)
        self.data = np.empty((self.n_bloc, self.n_plat))

    def seek(self, loc):
        '''
        move the reading head
        '''

        dist = np.abs(self.head_loc - loc)

        self.head_pos = loc

    def read(self, platter):
        '''
        reads from the specified platter
        '''
        return self.data[self.head_pos, platter]

    def write()
