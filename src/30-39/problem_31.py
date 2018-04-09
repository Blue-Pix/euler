# -*- coding: utf-8 -*-

''' Problem 31
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

合計2ポンドとなるコインの組み合わせの数
'''


def count_ways(target, coins):
    if len(coins) == 1:
        return 1
    count = 0
    quotient = target // coins[0]
    for times in range(quotient + 1):
        count += count_ways(target - coins[0] * times, coins[1:])
    return count


if __name__ == '__main__':

    TARGET = 200
    COINS = [200, 100, 50, 20, 10, 5, 2, 1]

    ways = count_ways(TARGET, COINS)
    print('In total, %d ways' % ways)
