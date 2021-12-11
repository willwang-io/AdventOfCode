dirs = [
    [1, 0], [-1, 0], [0, 1], [0, -1],
    [1, 1], [1, -1], [-1, 1], [-1, -1]
]


def flash(grid, i, j):
    if grid[i][j] < 9 or grid[i][j] == -1:
        return
    grid[i][j] = -1
    for a, b in dirs:
        x, y = a + i, b + j
        if x < 0 or y < 0 or x >= 10 or y >= 10 or grid[x][y] == -1:
            continue
        grid[x][y] += 1
        if grid[x][y] >= 9:
            flash(grid, x, y)


def solve(lst):
    arr = []
    first_all_flash = 0
    while True:
        for i in range(10):
            for j in range(10):
                flash(lst, i, j)
        for i in range(10):
            for j in range(10):
                lst[i][j] += 1
        flash_cnt = sum([i.count(0) for i in lst])
        if flash_cnt == 10 * 10:
            break
        first_all_flash += 1
        arr.append(flash_cnt)

    print(sum(arr[:100]))
    print(first_all_flash + 1)


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            line = list(line.strip())
            lst.append(list(map(int, line)))
    solve(lst)


if __name__ == '__main__':
    main()
