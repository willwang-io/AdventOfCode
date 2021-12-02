def part1(lst):
    pos, depth = 0, 0
    for opt, val in lst:
        if opt == 'forward':
            pos += val
        elif opt == 'down':
            depth += val
        else:
            depth -= val
    print(pos * depth)


def part2(lst):
    pos, depth, aim = 0, 0, 0
    for opt, val in lst:
        if opt == 'down':
            aim += val
        elif opt == 'up':
            aim -= val
        else:
            pos += val
            depth += aim * val
    print(pos * depth)


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            opt, val = line.split()
            lst.append((opt, int(val)))
    part1(lst)
    part2(lst)


if __name__ == '__main__':
    main()
