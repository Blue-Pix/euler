# -*- coding: utf-8 -*-

''' Problem 15
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

20×20のマス目の左上をスタート、右下をゴールとした時、
経路は何通りあるか。ただし、右と下にしか進めないものとする。
'''


import math


if __name__ == '__main__':
    N = 40
    R = 20
    permutation = math.factorial(N) / math.factorial(N - R)
    answer = permutation / math.factorial(R)
    print('answer is %d' % answer)
