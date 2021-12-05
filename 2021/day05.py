def part1(lst):
    grid = [0] * 1000000
    for x1, y1, x2, y2 in lst:
        if not (x1 == x2 or y1 == y2):
            continue
        while x1 != x2:
            grid[y1 * 1000 + x1] += 1
            x1 += 1 if x1 < x2 else -1
        while y1 != y2:
            grid[y1 * 1000 + x2] += 1
            y1 += 1 if y1 < y2 else -1
        grid[y1 * 1000 + x2] += 1
    print(sum(i >= 2 for i in grid))


def part2(lst):
    grid = [0] * 1000000
    for x1, y1, x2, y2 in lst:
        if not (x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)):
            continue
        while x1 != x2 or y1 != y2:
            grid[y1 * 1000 + x1] += 1
            if x1 != x2:
                x1 += 1 if x1 < x2 else -1
            if y1 != y2:
                y1 += 1 if y1 < y2 else -1
        grid[y1 * 1000 + x2] += 1
    print(sum(i >= 2 for i in grid))


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            line = line.strip().split('->')
            x1, y1 = map(int, line[0].split(','))
            x2, y2 = map(int, line[1].split(','))
            lst.append([x1, y1, x2, y2])
    part1(lst)
    part2(lst)


if __name__ == '__main__':
    main()
