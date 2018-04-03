# -*- coding: utf-8 -*-

''' Problem 21
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

10000以下の友愛数の総和
'''


import numpy as np
from functools import reduce


# 約数の総和
def sum_of_divisors(num):
    factors = factoring(num)
    operands = []
    for divisor, power in factors.items():
        operands.append(sum([divisor ** i for i in range(power + 1)]))
    return reduce(lambda x, y: x * y, operands) + 1


# 真約数の総和
def sum_of_proper_divisors(num):
    return sum_of_divisors(num) - (1 + num)


# 素因数分解
def factoring(num):
    factors = {}
    divisor = 2
    power = 0
    while num > 1:
        if num % divisor != 0:
            if power != 0:
                factors[divisor] = power
            divisor += 1
            power = 0
        else:
            num = num / divisor
            power += 1
    factors[divisor] = power
    return factors


if __name__ == '__main__':

    check_list = {}
    _sum = 0

    for a in range(220, 10001):
        if a in check_list:
            continue

        b = sum_of_proper_divisors(a)
        if b < a or b == a:
            continue

        sum_b = sum_of_proper_divisors(b)
        if sum_b == a:
            _sum += a + b
            print('%d : %d is amicable pair.' % (a, b))

        check_list[a, b] = 0

    print('sum is %d' % _sum)
