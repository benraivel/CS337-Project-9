# (disk, platter, loc)
# FAT alternates disks every _ blocks

import numpy as np


class Disk:

    def __init__(self, n_platters=2, blocks=1000):
        '''
        create a disk
        '''

        self.head_pos = 0

        self.data = np.empty((blocks, n_platters))

    def seek(self, loc):
        '''
        move the reading head
        '''
        self.head_pos = loc

    def read(self, platter):
        '''
        reads from the specified platter
        '''
        return self.data[self.head_pos, platter]
