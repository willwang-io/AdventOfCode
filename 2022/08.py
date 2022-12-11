#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve():
    ans = ans2 = 0

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    grid = []

    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            cur = map(int, line.rstrip())
            grid.append(list(cur))

    m, n = len(grid), len(grid[0])
    
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            ok = False
            score = 1
            for a, b in dirs:
                x, y = i + a, j + b
                cur_score = 0
                while 0 <= x < m and 0 <= y < n:
                    cur_score += 1
                    if grid[x][y] >= grid[i][j]:
                        break
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        ok = True
                    x += a
                    y += b
                score *= cur_score
            if ok:
                ans += 1
            ans2 = max(ans2, score)

    print(ans + 2 * m + 2 * (n - 2))
    print(ans2)
                    

def main():
    solve()


if __name__ == '__main__':
    main()
