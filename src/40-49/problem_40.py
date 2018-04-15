# -*- coding: utf-8 -*-

''' Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

正の整数を連結してゆき、1番目、10番目、100番目、1000番目、10000番目、100000番目、1000000番目の数字の積を求める。
'''


from functools import reduce


if __name__ == '__main__':

    num = 1
    concatenated = ''

    while True:
        concatenated += str(num)
        if len(concatenated) > 10 ** 6:
            break
        num += 1

    _product = reduce(lambda x, y: x * y, [int(concatenated[10 ** i - 1]) for i in range(7)])
    print('answer is %d' % _product)
