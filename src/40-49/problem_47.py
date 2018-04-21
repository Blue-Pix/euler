# -*- coding: utf-8 -*-

''' Problem 47
The first two consecutive numbers to have two distinct prime factors are:

$14 = 2 × 7$
$15 = 3 × 5$

The first three consecutive numbers to have three distinct prime factors are:

$644 = 2^2 × 7 × 23$
$645 = 3 × 5 × 43$
$646 = 2 × 17 × 19$.

Find the first four consecutive integers to have four distinct prime factors each.
What is the first of these numbers?

4つの素因数を持つ数が4連続で現れるのはいつか
'''


from math import sqrt
import time


def is_prime(num, primes):
    upper_bound = int(sqrt(num))
    for divisor in primes:
        if divisor > upper_bound:
            return True
        if num % divisor == 0:
            return False
    return True


def factoring(num, primes):
    index = 0
    factors = set()
    while num != 1:
        factor = primes[index]
        if num % factor == 0:
            num, _ = divmod(num, factor)
            factors.add(factor)
        else:
            index += 1
    return factors


def find_consecutive(primes, length):
    # between two primes
    prime_diff = primes[-1] - primes[-2]
    if prime_diff <= length:
        return None

    _count = 0
    for i in range(0, prime_diff):
        target = primes[-2] + (i + 1)
        factors = factoring(target, primes)
        if len(factors) == LENGTH:
            _count += 1
            if _count == length:
                return target - 3
        else:
            _count = 0
            # no more n consecutive numbers remain
            if (primes[-1] - primes[-2]) - (i + 1) < LENGTH:
                break
    return None


if __name__ == '__main__':
    
    start = time.time()
    primes = [2]
    num = 3
    LENGTH = 4
    target = None

    while True:
        if is_prime(num, primes):
            primes.append(num)
            target = find_consecutive(primes, LENGTH)
            if target is not None:
                print('answer is %d' % target)
                break
        num += 1
    print(time.time() - start)