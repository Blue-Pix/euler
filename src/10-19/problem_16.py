# -*- coding: utf-8 -*-

''' Problem 16
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

2の1,000乗の各桁の総和を求める
'''


if __name__ == '__main__':
    src = 2 ** 1000
    _sum = reduce(lambda x, y: int(x) + int(y), str(src))
    print('answer is %d' % _sum)
