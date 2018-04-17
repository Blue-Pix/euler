# -*- coding: utf-8 -*-

''' Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?

英単語をアルファベットの順番の和でスコア化した時に三角数となる単語の数
'''


import string


def triangle_numbers(threshold):
    n = 1
    tn = []
    while True:
        num = n * (n + 1) // 2
        if num > threshold:
            return tn
        tn.append(num)
        n += 1


if __name__ == '__main__':

    ALPHABETS = {letter: index + 1 for index, letter in enumerate(list(string.ascii_uppercase))}

    with open('./problem_42.txt') as f:
        words = f.read().replace('"', '').split(',')

    letter_sum = [sum([ALPHABETS[letter] for letter in word]) for word in words]
    _triangle_numbers = triangle_numbers(max(letter_sum))
    triangle_words = [_sum for _sum in letter_sum if _sum in _triangle_numbers]

    print('answer is %d' % len(triangle_words))
