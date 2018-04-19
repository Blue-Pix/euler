# -*- coding: utf-8 -*-

''' Problem 32
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual,
as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way
so be sure to only include it once in your sum.

乗数と被乗数と積の3つの数をもって1~9のパンデジタル数となる数の、積の総和
'''


from itertools import permutations
from functools import reduce
from math import sqrt


def is_prime(num):
    for divisor in range(2, int(sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True


def has_duplicate_digit(num):
    digits = {digit for digit in str(num)}
    if len(str(num)) == len(digits):
        return False
    return True


def remain_digits(num, digits):
    used = {digit for digit in str(num)}
    return set([str(i) for i in digits]).difference(used)


def is_pandigital_product(product, remain_digits):
    _permutations = permutations(remain_digits)
    for permutation in _permutations:
        # 1 digit * 4 digit
        multiplicand = int(permutation[0])
        multiplier = int(reduce(lambda x, y: x + y, permutation[1:]))
        if multiplicand * multiplier == product:
            return (multiplicand, multiplier)
        # 2 digit * 3 digit
        multiplicand = int(reduce(lambda x, y: x + y, permutation[:2]))
        multiplier = int(reduce(lambda x, y: x + y, permutation[2:]))
        if multiplicand * multiplier == product:
            return (multiplicand, multiplier)
    return None


if __name__ == '__main__':
    
    DIGITS = range(1, 10)
    _sum = 0

    not_prime_numbers = [num for num in range(3, 10000) if is_prime(num) is False]
    not_duplicate_not_prime_numbers = [num for num in not_prime_numbers if has_duplicate_digit(num) is False]

    for num in range(1000, 10000):
        remain = remain_digits(num, DIGITS)
        if len(remain) != 5:
            continue
        multipliers = is_pandigital_product(num, remain)
        if multipliers is not None:
            _sum += num
            print('%d * %d = %d' % (multipliers[0], multipliers[1], num))

    print('sum is %d' % _sum)
