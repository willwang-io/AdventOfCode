def main():
    dir = {'v': (1, 0), '^': (-1, 0), '>': (0, 1), '<': (0, -1)}
    line = open('in').read().strip('\n')
    seen = [(0, 0)]
    i, j = 0, 0
    ans = 0
    for k in range(0, len(line), 2):
        x, y = dir[line[k]]
        i += x
        j += y
        if (i, j) not in seen:
            seen.append((i, j))

    i, j = 0, 0
    r_seen = [(0, 0)]
    for k in range(1, len(line), 2):
        x, y = dir[line[k]]
        i += x
        j += y
        if (i, j) not in r_seen:
            ans += 1
            r_seen.append((i, j))
    print(len(set(seen) | set(r_seen)))
    # print(len(seen) + len(r_seen) - 1)

if __name__ == '__main__':
    main()