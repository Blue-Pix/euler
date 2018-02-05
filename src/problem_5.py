# -*- coding: utf-8 -*-

''' Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

1から20までの全ての整数で割り切れる最小の正数を求める
'''

import numpy as np


# greatest common divisor
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a


# least common multiple
def lcm(a, b):
  return a * b / gcd(a, b)


if __name__ == '__main__':
    src = range(2, 41)
    common_multiple = 1  # initialized by 1
    for i in src:
        new_common_multiple = lcm(common_multiple, i)
        print('lcm of %d and %d is %d' % (common_multiple, i, new_common_multiple))
        common_multiple = new_common_multiple

    print('answer is %d' % common_multiple)
