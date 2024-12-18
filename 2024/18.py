def helper(grid, N):
    q = [(0, 0)]
    steps = 0
    seen = set()
    while q:
        sz = len(q)
        for _ in range(sz):
            x, y = q.pop(0)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            if x == N - 1 and y == N - 1:
                return True
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and grid[ny][nx] == 0:
                    q.append((nx, ny))
        steps += 1
    return False
def main():
    N = 71
    UP = 1024
    grid = [[0] * N for _ in range(N)]
    with open('in.txt', 'r') as f:
        lines = f.readlines()
    for line in lines[UP + 1:]:
        x, y = line.split(',')
        x, y = int(x), int(y)
        grid[y][x] = 1
        if not helper(grid, N):
            print(x, y)
            return
    

if __name__ == '__main__':
    main()