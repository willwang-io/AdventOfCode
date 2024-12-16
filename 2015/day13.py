from itertools import permutations
from collections import defaultdict

def compute(perm, cnt):
    ans = 0
    for i in range(len(perm)):
        ans += cnt[perm[i]][perm[(i + 1) % len(perm)]]
        ans += cnt[perm[i]][perm[(i - 1) % len(perm)]]
    return ans

def main():
    with open('in.txt', 'r') as f:
        data = f.readlines()
    people = set()
    cnt = defaultdict(dict)
    for line in data:
        line = line.strip()
        line = line.replace(' would ', ' ').replace(' happiness units by sitting next to ', ' ').rstrip('.')
        a, opr, val, b = line.split(' ')
        val = int(val) * (1 if opr == 'gain' else -1)
        people.add(a)
        people.add(b)
        cnt[a][b] = val

    people.add('Me')
    for p in people:
        cnt[p]['Me'] = 0
        cnt['Me'][p] = 0
    
    ans = 0
    for perm in permutations(cnt.keys()):
        ans = max(ans, compute(perm, cnt))
    print(ans)

if __name__ == '__main__':
    main()
