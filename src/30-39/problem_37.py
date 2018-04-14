# -*- coding: utf-8 -*-

''' Problem 37
The number 3797 has an interesting property.
Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes
that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

11ある切り捨て可能素数の総和
'''

import time
from math import sqrt


def is_prime(target, divisors):
    upper_bound = int(sqrt(target))
    for divisor in divisors:
        if divisor > upper_bound:
            break
        if target % divisor == 0:
            return False
    return True


def is_truncatable_prime(num, prime_numbers):
    str_num = str(num)

    if str_num[1:].find('2') > 0:
        return False
    if str_num[1:].find('4') > 0:
        return False
    if str_num[1:].find('5') > 0:
        return False
    if str_num[1:].find('6') > 0:
        return False
    if str_num[1:].find('8') > 0:
        return False

    if str_num[0] in ['4', '6', '8', '9', '1']:
        return False


    # left to right
    for i in range(len(str_num) - 1):
        truncated_num = str_num[i + 1:]
        if int(truncated_num) not in prime_numbers:
            return False
    # right to left
    for i in range(len(str_num) - 1):
        truncated_num = str_num[:len(str_num) - (i + 1)]
        if int(truncated_num) not in prime_numbers:
            return False
    return True


if __name__ == '__main__':
    start = time.time()
    prime_numbers = [2]
    NOT_TRUNCATABLE_PRIMES = {2, 3, 5, 7}
    truncatable_primes = []
    num = 3

    while True:
        if is_prime(num, prime_numbers):
            prime_numbers.append(num)
            if num not in NOT_TRUNCATABLE_PRIMES and is_truncatable_prime(num, prime_numbers):
                truncatable_primes.append(num)
                print(num)
                if len(truncatable_primes) == 11:
                    break
        num += 2

    print('sum is %d' % sum(truncatable_primes))
    print(time.time() - start)