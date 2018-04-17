# -*- coding: utf-8 -*-

''' Problem 43
The number, 1406357289, is a 0 to 9 pandigital number
because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4 = 406 is divisible by 2
d3d4d5 = 063 is divisible by 3
d4d5d6 = 635 is divisible by 5
d5d6d7 = 357 is divisible by 7
d6d7d8 = 572 is divisible by 11
d7d8d9 = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

以上の性質を満たす0~9のパンデジタル数の総和
'''


from itertools import permutations


def convert_list_to_int(_list):
    return int(''.join(map(str, _list)))


def pre_check(digit_list):
    # non leading 0
    if digit_list[0] == 0:
        return False
    # divisble by even number
    if digit_list[3] not in {0, 2, 4, 6, 8}:
        return False
    # divisible by 5
    if digit_list[5] != 5:
        return False
    return True


def is_divisible(digit_list):
    DIVISORS = [17, 13, 11, 7, 5, 3, 2]
    offset = len(digit_list)
    for index, divisor in enumerate(DIVISORS):
        sub = convert_list_to_int(digit_list[offset - index - 3:offset - index])
        if sub % divisor != 0:
            return False
    return True


if __name__ == '__main__':

    src = list(permutations(range(10)))
    target = set()

    for digit_list in src:
        if pre_check(digit_list) and is_divisible(digit_list):
            num = convert_list_to_int(digit_list)
            target.add(int(num))

    print('sum is %d' % sum(target))
