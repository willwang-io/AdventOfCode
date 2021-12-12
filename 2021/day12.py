from collections import defaultdict


def part1(graph):
    paths = []

    def dfs(cur):
        if cur[-1] == 'end':
            paths.append(cur[:])
            return
        for nxt in graph[cur[-1]]:
            if nxt.islower() and nxt in cur:
                continue
            cur.append(nxt)
            dfs(cur)
            cur.pop()
    dfs(['start'])
    print(len(paths))


def part2(graph):
    paths = []

    def dfs(cur):
        if cur[-1] == 'end':
            paths.append(cur[:])
            return
        for nxt in graph[cur[-1]]:
            if nxt == 'start' or (
                    nxt.islower() and
                    nxt in cur and
                    any(cur.count(i) == 2 for i in cur if i.islower())
            ):
                continue
            cur.append(nxt)
            dfs(cur)
            cur.pop()

    dfs(['start'])
    print(len(paths))


def main():
    graph = defaultdict(list)
    with open('temp.txt') as file:
        for line in file:
            x, y = line.strip().split('-')
            graph[x].append(y)
            graph[y].append(x)
    part1(graph)
    part2(graph)


if __name__ == '__main__':
    main()
