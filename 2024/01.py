from collections import Counter
with open("in.txt", "r") as f:
    data = f.readlines()
    x = []
    y = []  
    for line in data:
        a, b = map(int, line.strip().split("   "))
        x.append(a)
        y.append(b)
    x = sorted(x)
    y = sorted(y)
    print(sum([abs(x[i] - y[i]) for i in range(len(x))]))
    cnt = Counter(y)
    ans = 0
    for i in x:
        ans += cnt[i] * i
    print(ans)

