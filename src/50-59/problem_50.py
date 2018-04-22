# -*- coding: utf-8 -*-

''' Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

100万以下で、連続する素数の和として表せる素数の内、和の項が最長となるもの
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


def prime_numbers(upper_bound):
    prime_numbers = [2]
    target = 3
    while target < upper_bound:
        if is_divisible(target, prime_numbers) is False:
            prime_numbers.append(target)
        target += 2
    return prime_numbers


def assume_max_length(primes):
    _sum = 0
    max_prime = primes[-1]
    for index, prime in enumerate(primes):
        _sum += prime
        if _sum > max_prime:
            return index
    return len(primes) - 1


def sum_of_consecutive_primes(primes, length):
    start_upper_bound = len(primes) - length
    max_prime = primes[-1]
    for start in range(start_upper_bound):
        _sum = sum(primes[start: start + length])
        if _sum > max_prime:
            return None
        if _sum in primes:
            return _sum
    return None


if __name__ == '__main__':

    UPPER_BOUND = 10 ** 6
    primes = prime_numbers(UPPER_BOUND)
    max_length = assume_max_length(primes)

    for length in range(max_length, 21, -1):
        _sum = sum_of_consecutive_primes(primes, length)
        if _sum is not None:
            print('sum of %d consecutive primes: %d' % (length, _sum))
            break
