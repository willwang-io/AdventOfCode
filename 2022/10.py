#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    x = 1
    lst = []

    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.rstrip().split()

            lst.append(x)
            if line[0] == 'addx':
                lst.append(x)
                x += int(line[1])

        lst.append(x)

        print(sum(i * lst[i - 1] for i in [20, 60, 100, 140, 180, 220]))

        for i in range(6):
            for j in range(40):
                x = lst[i * 40 + j]
                print('#' if x - 1 <= j <= x + 1 else '.', end=' ')
            print('')


def main():
    solve()


if __name__ == '__main__':
    main()
