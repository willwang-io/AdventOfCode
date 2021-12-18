def add_left(x, n):
    if not n:
        return x
    if type(x) is not list:
        return x + n
    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    if not n:
        return x
    if type(x) is not list:
        return x + n
    return [x[0], add_right(x[1], n)]


def explode(x, level):
    if type(x) is not list:
        return False, None, x, None
    if level == 4:
        return True, x[0], 0, x[1]
    a, b = x
    ok, left, a, right = explode(a, level + 1)
    if ok:
        return ok, left, [a, add_left(b, right)], None
    ok, left, b, right = explode(b, level + 1)
    if ok:
        return ok, None, [add_right(a, left), b], right
    return False, None, x, None


def split(x):
    if type(x) is not list:
        return (True, [x // 2, -(-x // 2)]) if x > 9 else (False, x)
    a, b = x
    ok, a = split(a)
    if ok:
        return ok, [a, b]
    ok, b = split(b)
    return ok, [a, b]


def solve(a, b):
    x = [a, b]
    while True:
        change, _, x, _ = explode(x, 0)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


def magnitude(x):
    if type(x) is not list:
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def main():
    file = open('input.txt', 'r')
    lst = list(map(eval, file.read().splitlines()))

    p1 = lst[0]
    for i in range(1, len(lst)):
        p1 = solve(p1, lst[i])
    print(magnitude(p1))

    p2 = float('-inf')
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                p2 = max(p2, magnitude(solve(lst[i], lst[j])))
    print(p2)


if __name__ == '__main__':
    main()
