from collections import Counter


def solve(s, rules, round):
    rules_cnt = Counter(s[i: i + 2] for i in range(len(s) - 1))
    for _ in range(round):
        temp = Counter()
        for k, v in rules_cnt.items():
            if k in rules:
                temp[k] -= v
                temp[k[0] + rules[k]] += v
                temp[rules[k] + k[1]] += v
        rules_cnt += temp
        
    cnt = Counter()
    for k, v in rules_cnt.items():
        cnt[k[0]] += v
        cnt[k[1]] += v
    cnt[s[0]] += 1
    cnt[s[-1]] += 1

    val = [i // 2 for _, i in cnt.items()]
    print(max(val) - min(val))


def main():
    rules = {}
    template = ''
    with open('input.txt') as file:
        template = file.readline().strip()
        file.readline()
        for line in file:
            k, v = line.strip().split(' -> ')
            rules[k] = v

    solve(template, rules, 10)
    solve(template, rules, 40)


if __name__ == '__main__':
    main()