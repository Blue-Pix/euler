# -*- coding: utf-8 -*-

''' Problem 46
It was proposed by Christian Goldbach
that every odd composite number can be written
as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite
that cannot be written
as the sum of a prime and twice a square?

ゴールドバッハ予想に反する最初の奇数は何か
'''


from math import sqrt


def is_prime(num, primes):
    upper_bound = int(sqrt(num))
    for divisor in primes:
        if divisor > upper_bound:
            return True
        if num % divisor == 0:
            return False
    return True


def goldbach(num, primes):
    for prime in primes:
        root = sqrt((num - prime) // 2)
        if root - int(root) == 0:
            print('%d = %d + 2 * %d^2' % (num, prime, root))
            return True
    return False


if __name__ == '__main__':

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    num = 35

    while True:
        # prime
        if is_prime(num, primes):
            primes.append(num)
            num += 2
            continue
        # composite
        if goldbach(num, primes[1:]) is False:
            print('answer is %d' % num)
            break
        num += 2
