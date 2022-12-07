#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Can't think something smarter, so I actually implement this file system...
# During the process of input, each directory only remember its size, lastly,
# use post-order traversal to update all parents' size. Once the root has the 
# total size, part 1 and part 2 are just some simply traversal the file system. 

class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.children = {}


def solve():
    root = Dir('/')
    p = root

    with open('input.txt', encoding='utf-8') as f:

        lines = [line.rstrip() for line in f]

        for line in lines:
            if line[0] == '$':
                x = line.split()[1:]
                if x[0] == 'ls':
                    continue
                if x[1] == '..':
                    p = p.parent
                elif x[1] == '/':
                    p = root
                else:
                    p.children[x[1]] = Dir(x[1])
                    p.children[x[1]].parent = p
                    p = p.children[x[1]]
            else:
                a, b = line.split()
                if a == 'dir':
                    if b not in p.children:
                        p.children[b] = Dir(b)
                        p.children[b].parent = p
                else:
                    p.size += int(a)


    def get_total_space(node):
        if not node.children:
            return node.size
        for child in node.children.values():
            node.size += get_total_space(child) 
        return node.size


    total = get_total_space(root)


    def part1(node):
        if not node:
            return 0
        ans = 0
        if node.size < 100000:
            ans += node.size
        for child in node.children.values():
            ans += part1(child)
        return ans


    def part2(node):
        if not node:
            return 70000000
        ans = 70000000
        if node.size + 70000000 - total > 30000000:
            ans = node.size
        for child in node.children.values():
            ans = min(ans, part2(child))
        return ans


    print(part1(root))
    print(part2(root))


def main():
    solve()


if __name__ == '__main__':
    main()
