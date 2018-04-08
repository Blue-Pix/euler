# -*- coding: utf-8 -*-

''' Problem 28
Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

1001 × 1001 の螺旋状に並んだ数の対角線状の数字の総和
'''


def diagonal_sum_of_square(s):
    # s: square size
    # g: greatest number of previous square
    if s == 1:
        return 1
    g = (s - 2) ** 2
    return 4 * g + 10 * (s - 1)


if __name__ == '__main__':
    square_size = range(1, 1002, 2)
    _sum = sum([diagonal_sum_of_square(s) for s in square_size])
    print('sum is %s' % _sum)
