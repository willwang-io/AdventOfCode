def solve(grid, folds):
    p1 = 0
    for k, fold in enumerate(folds, start=1):
        val = int(fold.split('=')[1])
        m, n = len(grid), len(grid[0])
        if fold[0] == 'y':
            for i in range(val):
                for j in range(n):
                    if grid[m - i - 1][j] != '.':
                        grid[i][j] = grid[m - i - 1][j]
            grid = grid[:val]
        else:
            for i in range(m):
                for j in range(val):
                    if grid[i][n - j - 1] != '.':
                        grid[i][j] = grid[i][n - j - 1]
            grid = [i[:val] for i in grid]
        if k == 1:
            p1 = sum(i.count('#') for i in grid)

    print(p1)
    [print(''.join(i)) for i in grid]


def main():
    # pre-process to find the max x-coord and max y-coord of the input file
    grid = [['.'] * 1311 for _ in range(895)]
    folds = []
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            if ',' in line:
                x, y = map(int, line.split(','))
                grid[y][x] = '#'
            elif 'fold' in line:
                _, _, axis = line.split()
                folds.append(axis)
    solve(grid, folds)


if __name__ == '__main__':
    main()
