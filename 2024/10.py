def part1(grid):
    rows, cols = len(grid), len(grid[0])
    total_score = 0

    def dfs(r, c, cur_height, seen):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in seen:
            return set()
        if grid[r][c] != cur_height:
            return set()
        if cur_height == 9:
            return {(r, c)}
        seen.add((r, c))
        return dfs(r + 1, c, cur_height + 1, seen) | dfs(r - 1, c, cur_height + 1, seen) | dfs(r, c + 1, cur_height + 1, seen) | dfs(r, c - 1, cur_height + 1, seen)


    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                reachable = dfs(r, c, 0, set())
                total_score += len(reachable)

    return total_score

def part2(grid):
    rows, cols = len(grid), len(grid[0])
    paths = set()
    def dfs(r, c, cur_height):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0
        if grid[r][c] != cur_height:
            return 0
        if cur_height == 9:
            return 1
        return dfs(r + 1, c, cur_height + 1) + dfs(r - 1, c, cur_height + 1) + dfs(r, c + 1, cur_height + 1) + dfs(r, c - 1, cur_height + 1)

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                ans += dfs(r, c, 0)
    print(ans)

def main():
    with open("in.txt", "r") as f:
        grid = [list(map(int, list(line.strip()))) for line in f]
    part2(grid)

if __name__ == "__main__":
    main()