def is_lowest(grid, i, j):
    cur = grid[i][j]
    if cur == 9 or \
            i - 1 >= 0 and grid[i - 1][j] < cur or \
            j - 1 >= 0 and grid[i][j - 1] < cur or \
            i + 1 < len(grid) and grid[i + 1][j] < cur or \
            j + 1 < len(grid[0]) and grid[i][j + 1] < cur:
        return False
    return True


def part1(lst):
    ans = 0
    m, n = len(lst), len(lst[0])
    for i in range(m):
        for j in range(n):
            if not is_lowest(lst, i, j):
                continue
            ans += lst[i][j] + 1
    print(ans)


def dfs(lst, i, j, prev, visited):
    if i < 0 or j < 0 or i >= len(lst) or j >= len(lst[0]):
        return 0
    if lst[i][j] == 9 or lst[i][j] < prev:
        return 0
    if f"{i}:{j}" in visited:
        return 0
    visited.add(f"{i}:{j}")
    ans = 1
    for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x, y = i + a, b + j
        ans += dfs(lst, x, y, lst[i][j], visited)
    return ans


def part2(lst):
    ans = []
    m, n = len(lst), len(lst[0])
    for i in range(m):
        for j in range(n):
            if not is_lowest(lst, i, j):
                continue
            size = dfs(lst, i, j, float('-inf'), set())
            ans.append(size)
    ans = sorted(ans)
    print(ans[-1] * ans[-2] * ans[-3])


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            line = list(map(int, line.strip()))
            lst.append(line)
    part1(lst)
    part2(lst)


if __name__ == '__main__':
    main()
