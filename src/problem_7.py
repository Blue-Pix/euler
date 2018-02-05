# -*- coding: utf-8 -*-

''' Problem 7
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

10001番目の素数を求める
'''

import numpy as np


if __name__ == '__main__':
    prime_number = [2]  # divided by prime numbers
    target = 3
    while True:
        is_prime = True
        for i in prime_number:
            if target % i == 0:
                is_prime = False
                break

        if is_prime is True:
            prime_number.append(target)
            print('%d is prime number' % target)
        target += 2  # every prime number is odd number, except for 2

        if len(prime_number) == 10001:
            print('10001th prime number is %d !' % prime_number[-1])
            break
