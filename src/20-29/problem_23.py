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

任意の2つの過剰数の和として表すことのできない数の総和
'''


from math import sqrt


def sum_of_proper_divisors(MAX):
    sum_list = [1] * (MAX + 1)
    for divisor in range(2, int(sqrt(MAX)) + 1):
        sum_list[divisor ** 2] += divisor
        for times in range(divisor + 1, MAX // divisor + 1):
            sum_list[divisor * times] += divisor + times
    return sum_list


def is_sum_of_two_abundant_numbers(num, abundant_numbers):
    for abundant_number in abundant_numbers:
        if abundant_number > num / 2:
            break
        if (num - abundant_number) in abundant_numbers:
            return True
    return False


if __name__ == '__main__':
    MAX = 28123
    sum_of_proper_divisors = sum_of_proper_divisors(MAX)
    abundant_numbers = set([num for num, _sum in enumerate(sum_of_proper_divisors) if _sum > num])
    abundant_numbers.remove(0)
    _sum = sum([num for num in range(MAX + 1) if not is_sum_of_two_abundant_numbers(num, abundant_numbers)])
    print('sum is %d' % _sum)
