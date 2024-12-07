from itertools import product

def generate_tuples(k):
    return list(product([0, 1, 2], repeat=k))

def solve(a, b):
    n = len(b) - 1
    tuples = generate_tuples(n)
    for t in tuples:
        ans = b[0]
        for j in range(n):
            if t[j] == 0:
                ans += b[j + 1]
            elif t[j] == 1:
                ans *= b[j + 1]
            else:
                ans = int(str(ans) + str(b[j + 1]))
        if ans == a:
            return a
    return 0


def main():
    ans = 0
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            a, b = line.split(': ')
            a = int(a)
            b = [int(x) for x in b.split()]
            ans += solve(a, b)
    print(ans)

if __name__ == '__main__':
    main()
