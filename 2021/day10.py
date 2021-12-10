def solve(lst):
    ref = {'(': ')', '<': '>', '[': ']', '{': '}'}
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}

    ans = 0
    arr = []
    for s in lst:
        stk = []
        ok = True
        for i in s:
            if i in ref:
                stk.append(i)
            else:
                if not stk or ref[stk[-1]] != i:
                    ans += score[i]
                    ok = False
                    break
                else:
                    stk.pop()
        if not ok:
            continue
        cur = 0
        for e in stk[::-1]:
            cur = cur * 5 + points[e]
        arr.append(cur)
    arr = sorted(arr)

    print(ans)
    print(arr[len(arr) // 2])


def main():
    lst = []
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            lst.append(line)
    solve(lst)


if __name__ == '__main__':
    main()
