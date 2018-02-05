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


if __name__ == '__main__':
    # square
    src = np.array([i ** 2 for i in range(1, 1000)])
    found = False
    for i in range(0, len(src)):
        for j in range(i, len(src)):
            a = src[i]
            b = src[j]
            c = np.sqrt(a + b)
            # a**2 + b**2 = c**2 ?
            if c % 1 != 0:
                continue
            a = np.sqrt(a)
            b = np.sqrt(b)
            # a + b + c = 1000 ?
            if a + b + c != 1000:
                continue

            print('Pythagorean triplet is: %d**2 + %d**2 = %d' % (a, b, c))
            print('%d * %d * %d = %d' % (a, b, c, a * b * c))
            found = True

        if found is True:
            break
