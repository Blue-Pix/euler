# -*- coding: utf-8 -*-

''' Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

600851475143の最大素因数を求める
'''


if __name__ == '__main__':
    divisor = 3
    target = 600851475143
    while divisor < target:
        quotient, remainder = divmod(target, divisor)
        if remainder == 0:
            print('%d can be divided by %d' % (target, divisor))
            target = quotient
        else:
            divisor += 2
    print('largest prime factor is %d' % divisor)
