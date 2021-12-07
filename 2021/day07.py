def solve(lst):
    p1 = p2 = float('inf')
    for i in range(min(lst), max(lst) + 1):
        a = b = 0
        for x in lst:
            a += abs(i - x)
            n = abs(i - x)
            b += n * (n + 1) // 2
        p1 = min(p1, a)
        p2 = min(p2, b)
    print(p1)
    print(p2)


def main():
    with open('input.txt') as file:
        lst = list(map(int, (file.readline().strip().split(','))))
    solve(lst)


if __name__ == '__main__':
    main()
