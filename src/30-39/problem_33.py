# -*- coding: utf-8 -*-

''' Problem 33
The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting to simplify it
may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

ある任意の分数から、分母と分子で共通している数を除くと、元の分数と等しい値になることがある。
値が1より小さく、分母と分子がそれぞれ2桁の分数において、上記のケースが4つある。
その4つの分数の積の分母を求める。
'''


from fractions import Fraction
from itertools import chain
from functools import reduce


def cancel(numerator, denominator):
    if numerator % 10 == 0 or denominator % 10 == 0:
        return False
    n_digits = set(list(str(numerator)))
    d_digits = set(list(str(denominator)))
    common_digits = n_digits.intersection(d_digits)
    for digit in common_digits:
        if digit == str(numerator)[0]:
            canceled_numerator = int(str(numerator)[1])
        else:
            canceled_numerator = int(str(numerator)[0])
        if digit == str(denominator)[0]:
            canceled_denominator= int(str(denominator)[1])
        else:
            canceled_denominator = int(str(denominator)[0])

        if Fraction(canceled_numerator, canceled_denominator) == Fraction(numerator, denominator):
            return True
    return False


if __name__ == '__main__':
    src = range(10, 100)
    dest = [[(numerator, denominator) for numerator in src[:index] if cancel(numerator, denominator) is True] for index, denominator in enumerate(src)]
    dest = chain.from_iterable(dest)
    _product = reduce(lambda x, y: x * y, [Fraction(fraction[0], fraction[1]) for fraction in dest])
    print('product is %s' % _product)
