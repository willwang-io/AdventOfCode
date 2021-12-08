def str_comp(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    print(s1, s2)
    return s2 - s1


def part1(lst):
    ans = 0
    for a, b in lst:
        for e in b.split():
            x = len(set(e))
            if x == 2 or x == 4 or x == x == 3 or x == 7:
                ans += 1
    print(ans)


def part2(lst):
    ans = 0
    for X, Y in lst:
        # 1, 7, 4, (2, 3, 5), (0, 6, 9), 8
        a, b, c, d, e, f, g, h, i, j = sorted(map(set, X.split()), key=len)
        # middle, bottom left, up right
        temp1 = (j - g).union(j - h, j - i)
        # bottom left & right, top left & right
        temp2 = (j - d).union(j - e, j - f)

        top = (j - a).intersection(b)
        bottom = j - top.union(temp1, c)
        bottom_left = j - top.union(c, bottom)
        mid = temp1.intersection(j - temp2)
        top_left = j - a.union(top, bottom, bottom_left, mid)
        top_right = temp1 - mid.union(bottom_left)
        bottom_right = temp2 - bottom_left.union(top_left, top_right)

        ref = [
            j - mid,
            a,
            j - top_left - bottom_right,
            j - top_left - bottom_left,
            c,
            j - top_right - bottom_left,
            j - top_right,
            b,
            j,
            j - bottom_left
        ]
        cur = 0
        for k in Y.split():
            k = set(k)
            cur = cur * 10 + ref.index(k)
        ans += cur
    print(ans)


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            lst.append(line.strip().split(' | '))
    part1(lst)
    part2(lst)


if __name__ == '__main__':
    main()
