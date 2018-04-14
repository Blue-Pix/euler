# -*- coding: utf-8 -*-

''' Problem 35
The number, 197, is called a circular prime
because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

100万より小さい循環素数はいくつあるか
'''


from math import sqrt


def is_divisible(target, divisors):
    upper_bound = sqrt(target)
    for divisor in divisors:
        if divisor > upper_bound:
            break
        if target % divisor == 0:
            return True
    return False


def prime_numbers(threshold):
    prime_numbers = [2]
    target = 3
    while target < 1000000:
        if is_divisible(target, prime_numbers) is False:
            prime_numbers.append(target)
        target += 2
    return set(prime_numbers)


def check_circular_prime(num, digit_list, checked, prime_numbers):
    _count = 1

    head = digit_list.pop(0)
    digit_list.append(head)

    while True:
        shifted_num = int(''.join(map(str, digit_list)))

        if shifted_num == num:
            return _count

        checked.add(shifted_num)

        if shifted_num not in prime_numbers:
            return 0

        _count += 1
        head = digit_list.pop(0)
        digit_list.append(head)


if __name__ == '__main__':
    THRESHOLD = 10 ** 6
    prime_numbers = prime_numbers(THRESHOLD)

    NOT_PRIME_DIGITS = {0, 2, 4, 5, 6, 8}
    checked = set()
    _count = 2 # initialized for 2 and 5

    for num in prime_numbers:
        digit_list = [int(digit) for digit in str(num)]

        if len(set(digit_list).intersection(NOT_PRIME_DIGITS)) != 0:
            continue

        if num in checked:
            continue

        _count += check_circular_prime(num, digit_list, checked, prime_numbers)

    print('answer is %d' % _count)
