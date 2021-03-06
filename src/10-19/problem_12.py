# -*- coding: utf-8 -*-

''' Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

500個以上の約数を持つ最初の三角数を求める
'''

import math


def count_divisors(src):
    divisors = 1
    i = 2
    while i < math.ceil(math.sqrt(src)):
        counter = 0
        while src % i == 0:
            counter += 1
            src = src / i
        divisors = divisors * (counter + 1)

        i = 3 if i == 2 else i + 2

        if src == 1:
            return divisors

    return divisors * 2


def triangle_number(n):
    return n * (n + 1) / 2


if __name__ == '__main__':
    n = 1
    while True:
        if n % 2 == 0:
            divisors = count_divisors(n / 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) / 2)

        if (divisors > 500):
            triangle_number = triangle_number(n)
            print('answer is %d' % triangle_number)
            break

        n += 1
