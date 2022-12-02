#!/usr/bin/env python
# -*- coding: utf-8 -*-

# the code was cleaned after submit

def solve():
    ans, ans2 = 0, 0
    pts = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    win = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'}
    lose = {'A': 'Y', 'B': 'Z', 'C': 'X'}


    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            p, q = line.strip('\n').split()

            ans += (0 if win[p] == q else 3 if draw[q] == p else 6) + pts[q]
            ans2 += 6 + pts[lose[p]] if q == 'Z' else pts[win[p]] if q == 'X' else 3 + pts[draw[p]]
            
    print(ans)
    print(ans2)

def main():
    solve()


if __name__ == '__main__':
    main()
