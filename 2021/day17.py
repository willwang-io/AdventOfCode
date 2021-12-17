def solve(x1, x2, y1, y2):
    p1, p2 = 0, 0
    for i in range(1, 200):
        for j in range(-200, 200):
            dx, dy = i, j
            x, y, max_y = 0, 0, 0
            ok = False
            for _ in range(500):
                x, y = x + dx, y + dy
                max_y = max(max_y, y)
                if x1 <= x <= x2 and y1 <= y <= y2:
                    ok = True
                    break
                dy -= 1
                if dx > 0:
                    dx -= 1
                elif dx < 0:
                    dx += 1
            if ok:
                p1 = max(p1, max_y)
                p2 += 1
    print(p1)
    print(p2)


def main():
    file = open('input.txt', 'r')
    line = file.readline().lstrip('target area: ').strip()
    x, y = line.split(', ')
    x1, x2 = map(int, x.lstrip('x=').split('..'))
    y1, y2 = map(int, y.lstrip('y=').split('..'))
    solve(x1, x2, y1, y2)


if __name__ == '__main__':
    main()
