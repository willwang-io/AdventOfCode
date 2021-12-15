def solve(grid):
    m, n = len(grid), len(grid[0])
    dist = [[float('inf')] * n for _ in range(m)]

    dist[0][0] = grid[0][0]

    def get_dist(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return float('inf')
        return dist[x][y]

    ok = True
    while ok:
        ok = False
        for i in range(m):
            for j in range(n):
                temp = grid[i][j] + min(get_dist(i + 1, j), get_dist(i - 1, j),
                                        get_dist(i, j + 1), get_dist(i, j - 1))
                if temp < dist[i][j]:
                    dist[i][j] = temp
                    ok = True
    return dist[m - 1][n - 1] - grid[0][0]


def main():
    grid = []
    with open('input.txt') as file:
        for line in file:
            line = list(map(int, list(line.strip())))
            grid.append(line)
    print(solve(grid))

    grids = [grid]
    for k in range(1, 9):
        copy = [x[:] for x in grid]
        for i in range(len(copy)):
            for j in range(len(copy[0])):
                copy[i][j] += k
                if copy[i][j] > 9:
                    copy[i][j] -= 9
        grids.append(copy)

    larger_grid = []
    for k in range(5):
        for i in range(len(grid)):
            cur = []
            for j in range(k, k + 5):
                cur.extend(grids[j][i])
            larger_grid.append(cur)
    print(solve(larger_grid))


if __name__ == '__main__':
    main()
