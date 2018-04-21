# -*- coding: utf-8 -*-

''' Problem 39
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

perimeter: 周囲の長さ
right angle triangle: 直角三角形
integral: 整数、全体

3辺の長さの合計pが1000以下になる数の内、3辺の数の組み合わせが最も多くなるもの
'''


from math import sqrt


def count_solutions(p, solutions):
    if p in solutions:
        solutions[p] += 1
    else:
        solutions[p] = 1
    return solutions


def search_b(a, c, square_dict, threshold):
    if square_dict[c] - square_dict[a] in square_dict.values():
        b = int(sqrt(square_dict[c] - square_dict[a]))
        if b <= a or a + b + c > threshold:
            return None
        return b
    return None


if __name__ == '__main__':

    THRESHOLD = 1000
    square_dict = {num: num ** 2 for num in range(1, THRESHOLD)}
    solutions = {}

    # c always even
    for c in range(2, THRESHOLD, 2):
        # a < c / 3
        for a in range(2, c // 3):
            # p exceeds 1000
            if c + a > THRESHOLD:
                break
            # search b^2
            b = search_b(a, c, square_dict, THRESHOLD)
            if b is not None:
                solutions = count_solutions(a + b + c, solutions)

    print('answer is %d' % sorted(solutions.items(), key=lambda x: x[1])[-1][0])
