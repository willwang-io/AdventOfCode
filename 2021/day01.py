def part1(lst):
    ans = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            ans += 1
    print(ans)


def part2(lst):
    lst2 = []
    for i in range(len(lst) - 2):
        lst2.append(sum(lst[i:i+3]))
    part1(lst2)


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            lst.append(int(line.strip()))
    part1(lst)
    part2(lst)


if __name__ == '__main__':
    main()
