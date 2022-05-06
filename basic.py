import numpy as np
from numpy.random import default_rng


def basic_genreq(addr, n, seed):
    '''
    returns a random list of 'n' requests to 'addr' locations
    '''
    # reset the rng
    rand = default_rng(seed)

    # return numpy array
    return rand.integers(addr, size=n)


def basic_fcfs(req):
    '''
    fcfs on basic req
    '''
    dist = 0
    next = req[0]
    req = np.delete(req, 0)

    while req.size > 0:

        prev = next
        next = req[0]

        req = np.delete(req, 0)

        dist += np.abs(next-prev)

    return dist


def basic_sstf(req, que_sz):
    '''
    sstf on basic req, picks from first que_sz
    '''
    dist = 0
    next = req[0]
    req = np.delete(req, 0)

    while req.size > 0:
        prev = next

        if req.size > que_sz:
            next_idx = np.argmax(req[:que_sz])
        else:
            next_idx = np.argmax(req)

        next = req[next_idx]

        req = np.delete(req, 0)

        dist += np.abs(next-prev)

    return dist


def basic_clook(req, que_sz):
    '''
    clook on basic req
    '''
    dist = 0
    next = 0
    req = np.delete(req, 0)

    while req.size > 0:

        # update previous pointer
        prev = next

        # get sorted list of requests in queue
        if req.size > que_sz:
            sorted = np.argsort(req[:que_sz])
            min_idx = np.argmin(req[:que_sz])

        else:  # remaining requests smaller than queue size
            sorted = np.argsort(req)
            min_idx = np.argmin(req)

        found_higher = False

        # search for a higher location in the queue
        for i in range(sorted.size):

            if req[sorted[i]] > prev:

                found_higher = True
                next = req[sorted[i]]
                req = np.delete(req, sorted[i])

                break

        # no higher location found
        if not found_higher:

            # return to the start
            next = req[min_idx]
            req = np.delete(req, min_idx)

        # update distance travled
        dist += np.abs(next-prev)

    return dist
