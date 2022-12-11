#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq


def solve():
    rules = [
        [lambda x: x * 13, 11, 3, 2],
        [lambda x: x + 2,  7, 6, 7],
        [lambda x: x + 6, 13, 3, 5],
        [lambda x: x * x, 5, 4, 5],
        [lambda x: x + 3, 3, 1, 7],
        [lambda x: x * 7, 17, 4, 1],
        [lambda x: x + 4, 2, 2, 0],
        [lambda x: x + 7, 19, 6, 0]
    ]

    worry_levels = [
        [57],
        [58, 93, 88, 81, 72, 73, 65],
        [65, 95],
        [58, 80, 81, 83],
        [58, 89, 90, 96, 55],
        [66, 73, 87, 58, 62, 67],
        [85, 55, 89],
        [73, 80, 54, 94, 90, 52, 69, 58]
    ]

    cnt = [0] * len(rules)

    mod = 1  # 3 for part 1 or just remove following 3 lines.
    for _, d, _, _ in rules:
        mod *= d

    for _ in range(10000):  # 20 for part 1
        for i, levels in enumerate(worry_levels):
            cnt[i] += len(levels)
            fun, d, t, f = rules[i]
            for j in map(fun, levels):
                # j //= 3  # for part 1
                worry_levels[t if j % d == 0 else f].append(j % mod)
            worry_levels[i].clear()

    a, b = heapq.nlargest(2, cnt)
    print(a * b)


def main():
    solve()


if __name__ == '__main__':
    main()
