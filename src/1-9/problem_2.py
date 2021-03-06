# -*- coding: utf-8 -*-

''' Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

400万未満の偶数のフィボナッチ数の和を求める
'''

import numpy as np


def createFibonacci(arr, _max):
    x = arr[-2]
    y = arr[-1]
    if x + y < _max:
        arr.append(x + y)
        createFibonacci(arr, _max)

if __name__ == '__main__':
    arr = [1, 2]
    MAX = 4000000
    createFibonacci(arr, MAX)
    arr = np.array(arr)
    _sum = np.sum(arr[(arr % 2) == 0])
    print('sum is %d' % _sum)
