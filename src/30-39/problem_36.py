# -*- coding: utf-8 -*-

''' Problem 36
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

10進数表記でも2進数表記でもパリンドローム数となる数
100万以下で以上の数の総和を求める
'''


def binary_palindromic(num):
    binary_num = int(bin(num).replace('0b', ''))
    return is_palindromic(binary_num)


def is_palindromic(num):
    digit_list = list(str(num))
    if len(digit_list) == 1:
        return True
    head_half = digit_list[:len(digit_list) // 2]
    compared = [digit for index, digit in enumerate(head_half) if digit == digit_list[-(index + 1)]]
    if len(compared) == len(head_half):
        return True
    return False


if __name__ == '__main__':
    THRESHOLD = 10 ** 6
    _sum = sum([num for num in range(1, THRESHOLD, 2) if is_palindromic(num) and binary_palindromic(num)])
    print('sum is %d' % _sum)
