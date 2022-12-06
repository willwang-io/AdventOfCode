#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():

    with open('input.txt', encoding='utf-8') as f:
        data = f.readline().rstrip()
        # change 14 to 4 for part 1
        for i in range(len(data)):
            cur = data[i: i + 14]
            if len(cur) == len(set(cur)):
                print(i + 14)
                return

def main():
    solve()


if __name__ == '__main__':
    main()
