from collections import defaultdict
import copy
def solve(grid):
    n, m = len(grid), len(grid[0])
    cnt = defaultdict(list)
    freq = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                continue
            cnt[grid[i][j]].append((i, j))
            freq.append((i, j))
    tmp = copy.deepcopy(grid)
    for _, v in cnt.items():
        for x1, y1 in v:
            for x2, y2 in v:
                if x1 == x2 or y1 == y2:
                    continue
                dx = x2 - x1
                dy = y2 - y1
                xx, yy = x1 - dx, y1 - dy
                while 0 <= xx < n and 0 <= yy < m:
                    tmp[xx][yy] = '#'
                    xx -= dx
                    yy -= dy
    res = 0
    for line in tmp:
        for v in line:
            if v != '.':
                res += 1
    print(res)  

def main():
    ans = 0
    grid = []
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            grid.append(list(line))
    solve(grid)

if __name__ == '__main__':
    main()

