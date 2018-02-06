# -*- coding: utf-8 -*-

''' Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a + b + c = 1000 になるようなピタゴラス数の組み合わせを求める
'''

import numpy as np


def is_square_number(num):
    return True if np.sqrt(num) % 1 == 0 else False


if __name__ == '__main__':
    src = np.array([i ** 2 for i in range(1, 1000)])
    answer = None
    length = len(src)
    for i in range(0, length):
        for j in range(i, length):
            a, b = src[i], src[j]
            if is_square_number(a + b) is False:
                continue
            c = np.sqrt(a + b)
            a = np.sqrt(a)
            b = np.sqrt(b)
            if (a + b + c == 1000) & (a < b < c):
                print('Pythagorean triplet is: %d**2 + %d**2 = %d**2' % (a, b, c))
                answer = a * b * c
                break
        if answer is not None:
            break
    print('product abc is %d' % answer)
