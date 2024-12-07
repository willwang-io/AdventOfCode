from collections import defaultdict, deque
import copy
import json
from functools import lru_cache

@lru_cache(maxsize=None)
def walk(grid, x, y):
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
    d = 0
    cnt = 0
    seen = set()
    n, m = len(grid), len(grid[0])
    while True:
        xx, yy = x + di[d], y + dj[d]
        seen.add((x, y))
        cnt += 1
        if cnt > n * m + 1:
            return True
        if 0 <= xx < n and 0 <= yy < m:
            if grid[xx][yy] == '#':
                d = (d + 1) % 4
            else:
                x, y = xx, yy
        else:
            return False

def main():
    grid = []
    with open('in.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            grid.append(list(line))

    x, y = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                x, y = i, j
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            tmp = copy.deepcopy(grid)
            if tmp[i][j] == '#':
                continue
            tmp[i][j] = '#'
            if walk(tmp, x, y):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
