# -*- coding: utf-8 -*-

''' Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

28123より大きい数字はsum of two abundant numbersとして表せる
sum of two abundant numbersとして表すことのできない最も大きい数字は28123未満である
'''


import numpy as np
from functools import reduce


def sum_of_divisors(num):
    factors = factoring(num)
    operands = []
    for divisor, power in factors.items():
        operands.append(sum([divisor ** i for i in range(power + 1)]))
    return reduce(lambda x, y: x * y, operands) + 1


def sum_of_proper_divisors(num):
    return sum_of_divisors(num) - (1 + num)


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


def is_abundant(num):
    _sum = sum_of_proper_divisors(num)
    if _sum > num:
        return True
    return False


if __name__ == '__main__':

    abundant_numbers_dict = {num: 0 for num in range(1, 28124) if is_abundant(num)}
    abundant_numbers = np.empty(len(abundant_numbers_dict))
    abundant_numbers[:] = abundant_numbers_dict.keys()

    sum_of_two_abundant_numbers = abundant_numbers + abundant_numbers.reshape((-1, 1))
    target = np.setdiff1d(np.arange(1, 28124), sum_of_two_abundant_numbers)

    _sum = np.sum(target)
    print('sum is %d' % _sum)
