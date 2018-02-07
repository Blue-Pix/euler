# -*- coding: utf-8 -*-

''' Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

3桁の数字2つから作れる最大のパリンドローム数を求める
'''

import numpy as np


def is_palindromic(num):
    num = str(num)
    l = len(num)
    for i in range(l / 2):
        if num[i] != num[-(i + 1)]:
            return False
    return True

if __name__ == '__main__':
    # [900]
    src = np.arange(100, 1000)
    # [900, 900]
    src = np.dot(src[:, np.newaxis], src[np.newaxis, :])
    # [8100]
    src = src.flatten()
    # sort desc
    src = np.sort(src)[::-1]

    for num in src:
        if is_palindromic(num) is True:
            print('%s is palindromic number!' % num)
            break
