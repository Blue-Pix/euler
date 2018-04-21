# -*- coding: utf-8 -*-

''' Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

1 <= n <= 1000の場合の、n^nの総和の下10桁
'''


if __name__ == '__main__':
    _sum = sum([num ** num for num in range(1, 1000)])
    print('last ten disits are %s' % str(_sum)[-10:])
