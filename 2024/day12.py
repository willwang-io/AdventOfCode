from collections import defaultdict

def area(grid, r, c, x, seen, no):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0
    if grid[r][c] != x:
        return 0
    if (r, c) in seen:
        return 0
    seen.add((r, c))
    ans = 1
    ok = True
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ans += area(grid, r + dr, c + dc, x, seen, no)
    return ans

def perimeter(grid, r, c, x, seen):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != x:
        return [(r, c)]
    if (r, c) in seen:
        return []
    seen.add((r, c))
    return (perimeter(grid, r + 1, c, x, seen) +
            perimeter(grid, r - 1, c, x, seen) +
            perimeter(grid, r, c + 1, x, seen) +
            perimeter(grid, r, c - 1, x, seen))

def main():
    grid = []
    with open("test.txt", "r") as f:
        lines = f.readlines()
    
    for line in lines:
        grid.append(list(line.strip()))

    st = []  # Changed from set to list
    global_seen = set()  # Shared seen set for both area and perimeter
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.' and (r, c) not in global_seen:
                char = grid[r][c]
                region_seen = set()
                no = []
                region_area = area(grid, r, c, char, region_seen, no)
                region_perimeter = perimeter(grid, r, c, char, set())
                st.append((char, region_area, len(region_perimeter)))
                global_seen.update(region_seen)  # Update global_seen to avoid reprocessing
    

    print(st)
    ans = sum(r * c for _, r, c in st)
    print(ans)

if __name__ == "__main__":
    main()