#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    lst = []
    total = 0
    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            x = line.strip('\n')
            if x == '':
                lst.append(total)
                total = 0
            else:
                total += int(x)
    lst.sort()
    print(lst[-1])
    print(sum(lst[-3:]))

def main():
    solve()


if __name__ == '__main__':
    main()

