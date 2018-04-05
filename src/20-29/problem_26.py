# -*- coding: utf-8 -*-

''' Problem 26
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

unit fraction: 単位分数（分母が自然数で分子が1）
numerator: 分子
denominator: 分母
decimal fraction: 小数

1000以下の自然数の単位分数で最長の循環節
'''


from decimal import Decimal, getcontext


def is_divisible(target, divisors):
    for i in divisors:
        if target % i == 0:
            return True
    return False


def prime_numbers():
    prime_numbers = {2: 0}
    target = 3
    while target < 1000:
        if is_divisible(target, prime_numbers.keys()) is False:
            prime_numbers[target] = 0
        target += 2
    return prime_numbers


def find_recurring_cycle(decimal_fraction_part, denominator):
    recurring_cycle = []
    for index, digit in enumerate(decimal_fraction_part):
        recurring_cycle.append(digit)
        length = None
        if len(recurring_cycle) > 1 and digit == recurring_cycle[0]:
            length = recurring_cycle_length(recurring_cycle, decimal_fraction_part, denominator)
        if length is not None:
            return length


def recurring_cycle_length(recurring_cycle, decimal_fraction_part, denominator):
    for index, digit in enumerate(reversed(recurring_cycle)):
        if digit != decimal_fraction_part[denominator - 1 - index]:
            return None
    print('%d: recurring cycle is %d' % (denominator, len(recurring_cycle) - 1))
    return len(recurring_cycle) - 1


if __name__ == '__main__':
    getcontext().prec = 2000
    prime_numbers = prime_numbers()
    longest_recurring_cycle = (7, 6)
    for denominator in prime_numbers.keys():
        decimal_fraction_part = list(str(Decimal(1) / Decimal(denominator)).split('.')[1])
        length = find_recurring_cycle(decimal_fraction_part, denominator)
        if length > longest_recurring_cycle[1]:
            longest_recurring_cycle = (denominator, length)
    print('longest recurring cycle is %d of 1 / %d' % (longest_recurring_cycle[1], longest_recurring_cycle[0]))
