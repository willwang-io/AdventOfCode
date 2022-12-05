#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Hard coded my input:
# [T]     [Q]             [S]        
# [R]     [M]             [L] [V] [G]
# [D] [V] [V]             [Q] [N] [C]
# [H] [T] [S] [C]         [V] [D] [Z]
# [Q] [J] [D] [M]     [Z] [C] [M] [F]
# [N] [B] [H] [N] [B] [W] [N] [J] [M]
# [P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
# [B] [W] [N] [P] [D] [V] [G] [L] [T]
#  1   2   3   4   5   6   7   8   9 

import re

def solve():
    lst = [
        'BPNQHDRT',
        'WGBJTV',
        'NRHDSVMQ',
        'PZNMC',
        'DZB',
        'VCWZ',
        'GZNCVQLS',
        'LGJMDNV',
        'TPMFZCG'
    ]

    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            a, b, c = map(int, re.findall(r'\d+', line.rstrip()))
            temp = lst[b - 1][-a:] # add [::-1] at the very end for part 1
            lst[b - 1] = lst[b - 1][:-a]
            lst[c - 1] += temp

    print(''.join(x[-1] for x in lst))


def main():
    solve()


if __name__ == '__main__':
    main()
