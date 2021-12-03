def part1(lst):
    cnt = list(zip(*lst))
    n = len(lst[0])
    gamma_rate = 0
    for i in range(len(cnt)):
        common = int(max(cnt[i], key=cnt[i].count))
        gamma_rate += common * 2 ** (n - i - 1)
    epsilon_rate = gamma_rate ^ ((1 << n) - 1)
    print(epsilon_rate * gamma_rate)


def part2(lst):
    generator, scrubber = lst[:], lst[:]
    n = len(lst[0])
    for i in range(n):
        cnt = list(zip(*generator))
        common = '1' if cnt[i].count('1') >= cnt[i].count('0') else '0'
        generator = [gen for gen in generator if gen[i] == common]
        if len(generator) == 1:
            break

    for i in range(n):
        cnt = list(zip(*scrubber))
        less_common = '0' if cnt[i].count('0') <= cnt[i].count('1') else '1'
        scrubber = [scrub for scrub in scrubber if scrub[i] == less_common]
        if len(scrubber) == 1:
            break
    print(int('0b' + generator[0], 2) * int('0b' + scrubber[0], 2))


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            lst.append(line.strip())
    part1(lst)
    part2(lst)


if __name__ == '__main__':
    main()
