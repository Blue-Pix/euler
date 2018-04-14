# -*- coding: utf-8 -*-

''' Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

各桁の階乗の総和が元の数と等しくなる数の総和を求める
'''


from math import factorial
from itertools import combinations_with_replacement


def assume_threshold():
    digit = 1
    while True:
        num = sum([9 * 10 ** (d - 1) for d in range(1, digit + 1)])
        factorial_sum = factorial(9) * digit
        if num > factorial_sum:
            return digit
        digit += 1


def factorial_sum_equal(digit_list, factorial_sum, zero_count):
    for digit in str(factorial_sum):
        if int(digit) in digit_list:
            digit_list.remove(int(digit))
        else:
            return False
    if len(digit_list) != 0:
        return False
    return True


if __name__ == '__main__':

    FACTORIALS = {digit: factorial(digit) for digit in range(10)}
    THRESHOLD = assume_threshold()
    combinations = combinations_with_replacement(range(10), THRESHOLD)
    dest = set()

    for combi in combinations:
        zero_count = ''.join(map(str, combi)).count('0')
        # how many digit '0' original number includes
        for z in range(zero_count + 1):
            # add sum of zero factorial
            factorial_sum = sum([FACTORIALS[digit] for digit in combi if digit != 0]) + z

            # Note: as 1! = 1 and 2! = 2 are not sums they are not included.
            if factorial_sum in (0, 1, 2):
                continue

            # adjust the number of digit '0'
            digit_list = [digit for digit in combi if digit != 0]
            digit_list += [0 for i in range(z)]

            equals = factorial_sum_equal(digit_list, factorial_sum, z)
            if equals is True:
                dest.add(factorial_sum)

    print('Numbers: %s' % dest)
    print('sum is %d' % sum(dest))
