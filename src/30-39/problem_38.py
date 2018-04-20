# -*- coding: utf-8 -*-

''' Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number
that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

(1, 2, ..., n)との積をつなげると1~9のパンデジタル数となる数を探す
連結した積が最大のものを求める
'''


from functools import reduce


def is_pandigital(num):
    digit_list = set(list(str(num)))
    return len(digit_list) == len(str(num))


def multiply(num):
    _length = 0
    _products = []
    for n in range(1, 10):
        _product = num * n
        # check product contains digit 0
        if str(_product).find('0') != -1:
            return None
        # check each product pandigital
        if is_pandigital(_product) is False:
            return None
        _length += len(str(_product))
        _products.append(_product)
        if _length >= 9:
            break
    if _length != 9:
        return None
    return _products


if __name__ == '__main__':

    UPPER_BOUND = 10 ** 5
    largest = 0

    for num in range(1, UPPER_BOUND):
        _products = multiply(num)
        if _products is not None:
            concatenated = reduce(lambda x, y: x + y, map(str, _products))
            if is_pandigital(concatenated):
                largest = max(largest, int(concatenated))

    print('answer is %d' % largest)
