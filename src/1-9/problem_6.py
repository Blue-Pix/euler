# -*- coding: utf-8 -*-

''' Problem 6
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

1~100の自然数の「平方の和」と「和の平方」の差を求める
'''

import numpy as np


if __name__ == '__main__':
    src = np.arange(1, 101)
    sum_of_square = np.sum(src ** 2)
    square_of_sum = np.sum(src) ** 2
    diff = np.abs(sum_of_square - square_of_sum)
    print('sum of square is %d' % sum_of_square)
    print('square of sum is %d' % square_of_sum)
    print('diff is %d' % diff)
