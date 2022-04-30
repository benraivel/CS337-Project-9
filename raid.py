# need to emulate one disc while preserving RAID 10 structure

# maybe use negative values to indicate EOF

import numpy as np
from disk import Disk
import random


class RAID1:

    def __init__(self, copies, platters, blocks):
        '''
        RAID 1 (exact copy)
        disks take read requests from a shared queue 
        '''

        self.disks

        self.request_queue = []

    def read_request(self, platter, block):
        '''
        add request to queue
        '''


class RAID0:

    def __init__(self, stripe_across=2, copies=2, grain_sz=5, platters=2, blocks=1000):
        '''
        RAID 0 (disk striping)
        '''
        self.gr_sz = grain_sz

        # NUMBER OF --------------------V
        self.n_strp = stripe_across     # disks to stripe across
        self.n_plat = platters          # platters on each disk
        self.n_bloc = blocks            # blocks on each platter
        self.n_copy = copies            # copies to create in RAID1

        # this is the amount of 'data' that can be held
        self.size = self.n_strp * self.n_plat * self.n_bloc

        # array of RAID1
        self.RAID1_array = np.empty(self.n_strp, dtype=RAID1)

        # loop over number of disks to stripe across
        for i in range(stripe_across):
            self.RAID1_array[i] = RAID1(self.n_copy, self.n_plat, self.n_bloc)

        self.init_FAT()

    def init_FAT(self, stripe_across, ):
        '''
        creates the File Allocation Table
        '''

        # FIRST 
        self.block_queue = []   # file allocation table
        self.empty_block = 0    # where to allocate new files from
        self.FAT = {}           # {filename : first block}


        disks = []  # temporary array
        
        # loop over RAID1s
        for d in range(self.strp):

            disk = []   # temporary array

            # loop over number of platters
            for p in range(self.plat):
                for b in range(blocks):
                    disk.append((d, p, b))

            random.shuffle(disk)
            disks.append(disk)

        while(len(disks[0]) > 0):

            for disk in disks:
                for _ in range(grain_sz):

                    self.FAT.append(disk.pop(0))

        for i in range(20):
            print(self.FAT[i])

    def write(self, filename, length):
        '''
        create a new file with filename and length
        '''

        # find the first free block
        file_start = self.FAT[self.FAT_index]

        # add to File table
        self.file_table[filename] = file_start]

        # loop for each block of the file
        for block in range(length):
            pass

    def modify():
        '''
        
        '''

    def request(self, filename):
        '''
        only need to read from one disk
        '''
        
        # add file to request queue


def main():

    RAID1()
    RAID1()


if __name__ == '__main__':
    main()
