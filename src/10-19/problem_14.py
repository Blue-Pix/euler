# -*- coding: utf-8 -*-

''' Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

コラッツの問題
1,000,000以下の自然数を初期値とする時の、最大のステップ数を生み出す初期値を求める
'''


def collatz(src):
    if src % 2 == 0:
        return src / 2
    return 3 * src + 1


def count(src, steps):
    dest = collatz(src)
    if dest not in steps:
        count(dest, steps)
    steps[src] = steps[dest] + 1
    return steps


if __name__ == '__main__':
    MAX = 10 ** 6
    answer = None
    longest_chain = 0
    steps = {1: 1}

    for i in range(MAX, 1, -1):
        if i in steps:
            continue
        steps = count(i, steps)
        if steps[i] > longest_chain:
            longest_chain = steps[i]
            answer = i

    print('longest chain is %d, which starts with %d' % (longest_chain, answer))
