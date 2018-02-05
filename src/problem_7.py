# -*- coding: utf-8 -*-

''' Problem 7
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

10001番目の素数を求める
'''

import numpy as np


def is_divisible(target, divisors):
    for i in divisors:
        if target % i == 0:
            return True
    return False


if __name__ == '__main__':
    prime_number = [2]
    target = 3
    while True:
        if is_divisible(target, prime_number) is False:
            if len(prime_number) == 10000:
                print('10001th prime number is %d !' % target)
                break
            prime_number.append(target)
            print('%d is prime number' % target)
        target += 2  # every prime number is odd number, except for 2
