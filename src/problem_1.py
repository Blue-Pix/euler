# -*- coding: utf-8 -*-

''' Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

3または5で割り切れる1000未満の自然数の和を求める
'''

import numpy as np

if __name__ == '__main__':
    src = np.arange(1, 1000)
    dest = src[(src % 3 == 0) | (src % 5 == 0)]
    sum = np.sum(dest)
    print('sum is %d' % sum)
