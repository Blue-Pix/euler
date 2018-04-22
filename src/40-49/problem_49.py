# -*- coding: utf-8 -*-

''' Problem 49
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

1. 全て素数であること
2. 同じ数字を用いた順列であること
3. 同じ数だけ増加していること。
以上の条件を満たす4桁の数字3つを求める。
'''


from math import sqrt
from itertools import permutations, combinations


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
    while target < threshold:
        if is_divisible(target, prime_numbers) is False:
            prime_numbers.append(target)
        target += 2
    return prime_numbers


def make_candidates(num, primes):
    _permutations = permutations(list(str(num)))
    candidates = set()
    for permutation in _permutations:
        new_num = int(''.join(map(str, permutation)))
        if new_num in primes:
            candidates.add(new_num)
            primes.remove(new_num)
    return candidates


def find_sequence(candidates):
    candidates = sorted(list(candidates))
    _combinations = combinations(candidates, 3)
    for combination in _combinations:
        if combination[1] - combination[0] == combination[2] - combination[1]:
            return combination
    return None


if __name__ == '__main__':

    primes = list(filter(lambda x: x > 1000, prime_numbers(10000)))

    for prime in primes:
        candidates = make_candidates(prime, primes)
        sequence = find_sequence(candidates)
        if sequence is not None:
            print(sequence)
