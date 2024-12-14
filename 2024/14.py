import re

N, M = 103, 101
# N, M = 7, 11

def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()
    lst = []
    grid = [[0] * M for _ in range(N)]
    for i, line in enumerate(lines):
        line = line.strip()
        pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
        match = re.match(pattern, line)
        if match:
            x, y, dx, dy = map(int, match.groups())
            lst.append((x, y, dx, dy))

    for i in range(1, 1000000000):
        for j, (x, y, dx, dy) in enumerate(lst):
            lst[j] = ((x + dx) % M, (y + dy) % N, dx, dy)

        grid = [[0] * M for _ in range(N)]
        for x, y, dx, dy in lst:
            grid[y][x] += 1
        # import os
        # import time
        # os.system('cls' if os.name == 'nt' else 'clear')
        mat = []
        ok = False
        for row in grid:
            cur = ''
            for r in row:
                if r > 0:
                    cur += '*'
                else:
                    cur += '.'
            if '*******************************' in cur:
                ok = True
        if ok:
            print(i)
            break
    
    # mid_x = N // 2
    # mid_y = M // 2
    # ans = [0, 0, 0, 0]
    # for i in range(N):
    #     for j in range(M):
    #         if i < mid_x and j < mid_y:
    #             ans[0] += grid[i][j]
    #         elif i < mid_x and j > mid_y:
    #             ans[1] += grid[i][j]
    #         elif i > mid_x and j < mid_y:
    #             ans[2] += grid[i][j]
    #         elif i > mid_x and j > mid_y:
    #             ans[3] += grid[i][j]
    # print(ans)
    # print(ans[0] * ans[1] * ans[2] * ans[3])


if __name__ == "__main__":
    main()