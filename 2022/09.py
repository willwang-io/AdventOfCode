#!/usr/bin/env python
# -*- coding: utf-8 -*-

# question summary: Given a list of element, A. In each step, A[i] will move to
# certain position based on where A[i - 1] moved for 1 < i < len(A). Notice A[0]
# always moves first.

def move(p, q):
    ax, ay = p
    bx, by = q
    diagonal = [[1, 1], [-1, 1], [1, -1], [-1, -1]]

    dist = abs(ax - bx) + abs(ay - by)

    # (Rule 2) two steps directly up, down, left, or right
    if dist == 2:
        if ax == bx:
            return [bx, by + 1] if ay > by else [bx, by - 1]
        if ay == by:
            return [bx + 1, by] if ax > bx else [bx - 1, by]

    # (Rule 3)
    if dist >= 3:
        for x, y in diagonal:
            tx, ty = bx + x, by + y
            dx, dy = abs(tx - ax), abs(ty - ay)
            if dx + dy == 1 or (dx == dy and dx + dy == 2):
                return [tx, ty]

    # (Rule 1) is touching; up, down, left, right, or diagonally
    return [bx, by]


def solve():
    n = 1000
    knots_len = 10  # 2 for part 1

    knots = [[n // 2, n // 2] for _ in range(knots_len)]
    dirs = {'R': (0, 1), 'U': (-1, 0), 'D': (1, 0), 'L': (0, -1)}
    visited = [0 for _ in range(n * n + 1)]

    with open('input.txt', encoding='utf-8') as f:
        for line in f.readlines():
            a, b = line.rstrip().split()
            for _ in range(int(b)):
                knots[0][0] += dirs[a][0]
                knots[0][1] += dirs[a][1]
                for j in range(1, knots_len):
                    knots[j] = move(knots[j - 1], knots[j])
                # 2D index to 1D
                visited[knots[-1][0] * 1000 + knots[-1][1]] = 1

    print(sum(visited))


def main():
    solve()


if __name__ == '__main__':
    main()
