# -*- coding: utf-8 -*-

''' Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

1から1,000まで単語として記述すると、何文字になるか
'''


TEN = 10
HUNDRED = 100
THOUSAND = 1000
WORDS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    TEN: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    HUNDRED: 'hundred',
    THOUSAND: 'thousand',
}


def convert_to_word(num):
    word = ''
    # 1000 ~ 9999
    quotient, remainder = divmod(num, THOUSAND)
    if quotient != 0:
        word += WORDS[quotient] + WORDS[THOUSAND]
    # 100 ~ 999
    quotient, remainder = divmod(remainder, HUNDRED)
    if quotient != 0:
        word += WORDS[quotient] + WORDS[HUNDRED]
        if remainder != 0:
            word += 'and'
    # 1 ~ 20
    if remainder < 20:
        word += WORDS[remainder]
    # 21 ~ 99
    else:
        quotient, remainder = divmod(remainder, TEN)
        if quotient != 0:
            word += WORDS[quotient * TEN] + WORDS[remainder]

    return word


if __name__ == '__main__':
    _len = 0
    for i in range(1, 1001):
        word = convert_to_word(i)
        _len += len(word)
        print('%d: %s' % (i, word))
    print('answer is %d' % _len)
