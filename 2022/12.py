#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve():
    with open('input.txt', encoding='utf-8') as f:
        grid = []
        for line in f.readlines():
            grid.append(list(map(lambda x: ord(x), line.rstrip())))

        q = []
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            q.append((i, 0))
            visited[i][0] = True
            if grid[i][0] == 83:
                grid[i][0] = 97

        ans = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                i, j = q.pop(0)
                for a, b in dirs:
                    ii, jj = i + a, j + b
                    if 0 <= ii < m and 0 <= jj < n and not visited[ii][jj]:
                        if grid[ii][jj] == 69:
                            return ans + 1
                        if grid[ii][jj] - grid[i][j] <= 1:
                            visited[ii][jj] = True
                            q.append((ii, jj))
            ans += 1

        return -1


def main():
    print(solve())


if __name__ == '__main__':
    main()
