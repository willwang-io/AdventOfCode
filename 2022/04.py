#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Notice: I replaced '-' and ',' in input.txt to spaces.

def solve():
    ans, ans2 = 0, 0

    with open('input.txt', encoding='utf-8') as f:
        for pair in f.readlines():
            a, b, c, d = map(int, pair.rstrip().split())

            if (c >= a and d <= b) or (c <= a and d >= b):
                ans += 1

            if a <= d and c <= b:
                ans2 += 1

    print(ans)
    print(ans2)


def main():
    solve()


if __name__ == '__main__':
    main()
