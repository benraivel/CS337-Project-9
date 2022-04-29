# need to emulate one disc while preserving RAID 10 structure

# maybe use negative values to indicate EOF

import numpy as np
from disk import Disk
import random


class RAID10:

    def __init__(self, stripe_across=2, copies=2, grain_sz=5, platters=2, blocks=1000):
        '''
        create a RAID of
        '''
        self.size = stripe_across * platters * blocks

        # Array of Inexpensive Disk objects
        self.disk_array = np.empty(copies, stripe_across)

        # loop over copies
        for i in range(copies):
            for j in range(stripe_across):

                self.disk_array[i][j] = disk.Disc(platters, blocks)

        # create a FAT (random linked list of locations)
        # locations are (disk, platter, loc)

        self.FAT = []
        disks = []
        for d in range(stripe_across):

            disk = []
            for p in range(platters):
                for b in range(blocks):

                    disk.append((d, p, b))

            random.shuffle(disk)
            disks.append(disk)

        while(len(disks[0]) > 0):

            for disk in disks:

                for _ in range(grain_sz):

                    self.FAT.append(disk.pop(0))

        print(self.FAT[:20])

    def write(self, filename, length):
        '''
        write needs to write to all discs
        '''
        pass
        # add to File table

    def read(self, filename):
        '''
        only need to read from one disk
        '''
        pass


def main():

    RAID10()
    RAID10()


if __name__ == '__main__':
    main()
