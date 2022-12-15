#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sand_drop(grid):
    x, y = 0, 500
    m, n = len(grid), len(grid[0])
    ok = False

    while 0 <= x < m and 0 <= y < n and not ok:
        if grid[x + 1][y] == '.':
            x += 1
        elif grid[x + 1][y] != '.' and grid[x + 1][y - 1] == '.':
            x += 1
            y -= 1
        elif grid[x + 1][y] != '.' and grid[x + 1][y + 1] == '.':
            y += 1
        else:
            ok = True
    grid[x][y] = 'o'


def solve():
    rocks = []
    max_y = -1

    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.rstrip().replace('->', ' ').replace(',', ' ')
            ranges = list(map(int, line.split()))
            rocks.append(ranges)

        grid = [['.' for _ in range(1000)] for _ in range(1000)]

        for rock in rocks:
            for i in range(2, len(rock) - 1, 2):
                x1, y1, x2, y2 = rock[i - 2: i + 2]
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        grid[y][x] = '#'
                max_y = max(max_y, y1, y2)

        ans = 0
        copy_grid = [r[:] for r in grid]
        while True:
            try:
                sand_drop(copy_grid)
                ans += 1
            except IndexError:
                break
        print(ans)

        for i in range(len(grid[0])):
            grid[max_y + 2][i] = '#'

        cnt = 0
        while grid[0][500] != 'o':
            sand_drop(grid)
            cnt += 1
        print(cnt)


def main():
    solve()


if __name__ == '__main__':
    main()
