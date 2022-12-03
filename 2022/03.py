#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_letters
from functools import reduce

def solve():
    priorities = '#' + ascii_letters
    ans, ans2 = 0, 0

    with open('input.txt', encoding='utf-8') as f:
        data = f.read().replace('\n', ' ').split()

        for x in data:
            a, b = set(x[:len(x) // 2]), set(x[len(x) // 2:])
            ans += priorities.index(next(iter(a & b)))

        for i in range(0, len(data), 3):
            y = reduce(lambda x, y: x & y, map(set, data[i:i+3]))
            ans2 += priorities.index(next(iter(y)))

    print(ans)
    print(ans2)


def main():
    solve()


if __name__ == '__main__':
    main()
