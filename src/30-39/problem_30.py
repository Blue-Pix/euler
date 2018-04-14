# -*- coding: utf-8 -*-

''' Problem 30
Surprisingly there are only three numbers
that can be written as the sum of fourth powers of their digits:

1634 = 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4
8208 = 8 ** 4 + 2 ** 4 + 0 ** 4 + 8 ** 4
9474 = 9 ** 4 + 4 ** 4 + 7 ** 4 + 4 ** 4
As 1 = 1 ** 4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers
that can be written as the sum of fifth powers of their digits.

各桁の5乗の和となる数の総和
'''


def equals_power_sum(num, power, powered_digits):
    _sum = sum([powered_digits[int(digit)] for digit in str(num)])
    if num == _sum:
        return True
    return False


def assume_threshold(power):
    digit = 1
    while True:
        num = sum([9 * 10 ** (d - 1) for d in range(1, digit + 1)])
        power_sum = 9 ** power * digit
        if num > power_sum:
            return power_sum
        digit += 1


if __name__ == '__main__':

    POWER = 5
    POWERED_DIGITS = [digit ** POWER for digit in range(10)]
    THRESHOLD = assume_threshold(POWER)

    src = range(2, THRESHOLD)
    dest = set([num for num in src if equals_power_sum(num, POWER, POWERED_DIGITS)])
    _sum = sum(dest)

    print('sum is %d' % _sum)
