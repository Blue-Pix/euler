# -*- coding: utf-8 -*-

''' Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

2,000,000未満の素数の和を求める
'''

import numpy as np
import time


if __name__ == '__main__':
    MAX = 2 * 10 ** 6
    src = np.array([0] * MAX)
    target = 3
    sum = 2
    while target < MAX:
        # if prime
        if src[target] == 0:
            # Sieve of Eratosthenes
            not_prime = range(0, MAX, target)
            src[not_prime] = 1
            # sum
            sum += target
        # check only odd number
        target += 2
    print('sum is %d' % sum)
