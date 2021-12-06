from collections import Counter


def solve(lst, day):
    cnt = Counter(lst)
    for i in range(day):
        temp = Counter()
        for k, v in cnt.items():
            if not k:
                temp[6] += v
                temp[8] += v
            else:
                temp[k - 1] += v
        cnt = temp
    print(sum(cnt.values()))


def main():
    with open('input.txt') as file:
        lst = list(map(int, (file.readline().strip().split(','))))
    solve(lst, 80)
    solve(lst, 256)


if __name__ == '__main__':
    main()
