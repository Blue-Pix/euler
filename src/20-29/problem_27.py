# -*- coding: utf-8 -*-

''' Problem 27
Euler discovered the remarkable quadratic formula:

n**2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n**2−79n+1601 was discovered,
which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.

最も多くの連続する素数を生み出す公式の係数a,b
'''


import numpy as np
import time


def is_divisible(target, divisors):
    for i in divisors:
        if target % i == 0:
            return True
    return False


def prime_numbers(threshold):
    prime_numbers = set([2])
    target = 3
    while target < threshold:
        if is_divisible(target, prime_numbers) is False:
            prime_numbers.add(target)
        target += 2
    return prime_numbers


if __name__ == '__main__':
    prime_numbers = prime_numbers(1000)
    answer = {'a': 0, 'b': 0, 'n': 0}
    for a in range(-999, 1000):
        # if n = 0, formula produces b
        for b in (list(prime_numbers) + [-num for num in prime_numbers]):
            n = 0
            while True:
                num = n ** 2 + a * n + b
                if num in prime_numbers:
                    n += 1
                    continue
                # if n = b, formula produces multiple of b
                if n == b - 1 or is_divisible(num, prime_numbers):
                    if n > answer['n']:
                        answer['a'] = a
                        answer['b'] = b
                        answer['n'] = n
                    break
                prime_numbers.add(num)
                n += 1
    print('a=%d, b=%d produces %d consecutive prime numbers' % (answer['a'], answer['b'], answer['n']))
    print('product of %d and %d is %d' % (answer['a'], answer['b'], answer['a'] * answer['b']))
