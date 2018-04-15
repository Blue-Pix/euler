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


if __name__ == '__main__':

    THRESHOLD = 1000
    square_dict = {num: num ** 2 for num in range(1, THRESHOLD)}
    square_list = square_dict.values()
    solutions = {}

    for c, c_square in square_dict.items():
        if THRESHOLD / 2 < c:
            break
        for a, a_square in square_dict.items():
            if c_square <= a_square:
                break
            if c + a > THRESHOLD:
                break
            if c_square - a_square in square_list:
                b = int(sqrt(c_square - a_square))
                if b < a:
                    break
                if a + b + c > THRESHOLD:
                    continue

                if a + b + c in solutions:
                    solutions[a + b + c] += 1
                else:
                    solutions[a + b + c] = 1

    print('answer is %d' % sorted(solutions.items(), key=lambda x: x[1])[-1][0])
