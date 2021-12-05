def solve(lst, part2=False):
    grid = [0] * 1000000
    for x1, y1, x2, y2 in lst:
        if x1 != x2 and y1 != y2 and (not part2 or abs(x1 - x2) != abs(y1 - y2)):
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
    solve(lst)
    solve(lst, part2=True)


if __name__ == '__main__':
    main()
