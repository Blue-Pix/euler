# -*- coding: utf-8 -*-

''' Problem 41
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

パンデジタル数かつ素数である最大の数
'''


import time
from itertools import permutations
from math import sqrt


def is_prime(target):
    upper_bound = int(sqrt(target))
    num = 3
    while num < upper_bound:
        if target % num == 0:
            return False
        num += 2
    return True


def largest_pandigital_prime(digit):
    _permutations = permutations(range(digit, 0, -1))
    for permutation in _permutations:
        if permutation[-1] in {2, 4, 5, 6, 8}:
            continue
        num = int(''.join(map(str, permutation)))
        if is_prime(num):
            return num
    return None


if __name__ == '__main__':
    for n in range(9, 1, -1):
        num = largest_pandigital_prime(n)
        if num is not None:
            print('answer is %d' % num)
            break
