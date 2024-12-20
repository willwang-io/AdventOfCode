import sys
from functools import cache
sys.setrecursionlimit(1000000)

grid = []
with open('in.txt', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

si, sj = 0, 0
ei, ej = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            si, sj = i, j
        if grid[i][j] == 'E':
            ei, ej = i, j

def solve(g):
    visited = set()
    actual = 9368
    ans = 0
    # @cache
    def dfs(i, j, dist, left=1):
        if i == ei and j == ej:
            return 0
        if i < 0 or i >= len(g) or j < 0 or j >= len(g[i]):
            return float('inf')
        if g[i][j] == '#' and left == 0:
            return float('inf')
        if (i, j) in visited:
            return float('inf')
        visited.add((i, j))
        ans = float('inf')
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + di, j + dj, dist + 1)
        visited.remove((i, j))
        return ans + 1
    return dfs(si, sj)

# cnt = 0
# max_saved = 0
# for i in range(1, len(grid) - 1):
#     print(i)
#     for j in range(1, len(grid[i]) - 1):
#         if grid[i][j] == '#':
#             cnt += 1
#             # grid[i][j] = '.'
#             # saved = solve(grid)
#             # if actual - saved >= 100:
#             #     max_saved = max(max_saved, actual - saved)
#             #     cnt += 1
#             # grid[i][j] = '#'
# print(cnt)
# print(max_saved)