# -*- coding: utf-8 -*-

''' Problem 23
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

0~9の順列を昇順に並べた時の100万番目
'''


from itertools import permutations


if __name__ == '__main__':
    _permutations = list(permutations(range(10)))
    print('answer is %s' % ''.join(map(str, _permutations[999999])))
