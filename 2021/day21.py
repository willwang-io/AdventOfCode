def part1(p1, p2):
    p1, p2 = p1 - 1, p2 - 1
    s1, s2 = 0, 0
    die = 0
    while True:
        p1 = (p1 + 3 * (die + 2)) % 10
        s1 += p1 + 1
        if s1 >= 1000:
            return s2 * (die + 3)
        p2 = (p2 + 3 * (die + 5)) % 10
        s2 += p2 + 1
        if s2 >= 1000:
            return s1 * (die + 6)
        die += 6


def part2(p1, p2, s1, s2, memo):
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1
    if (p1, p2, s1, s2) in memo:
        return memo[(p1, p2, s1, s2)]
    ans = (0, 0)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                nxt_p1 = (p1 + i + j + k) % 10
                nxt_s1 = s1 + nxt_p1 + 1
                a, b = part2(p2, nxt_p1, s2, nxt_s1, memo)
                ans = (ans[0] + b, ans[1] + a)
    memo[(p1, p2, s1, s2)] = ans
    return ans


def main():
    p1, p2 = 1, 2
    print(part1(p1, p2))
    print(max(part2(p1 - 1, p2 - 1, 0, 0, dict())))


if __name__ == '__main__':
    main()
