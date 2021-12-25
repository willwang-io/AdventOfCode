X = list(map(list, open('input.txt', 'r').read().splitlines()))

m, n = len(X), len(X[0])
step = 0

while True:
    copy = [x[:] for x in X]
    change1, change2 = False, False
    for i in range(m):
        for j in range(n):
            if X[i][j] == '>' and X[i][(j + 1) % n] == '.':
                copy[i][(j + 1) % n] = '>'
                copy[i][j] = '.'
                change1 = True
    X = [c[:] for c in copy]
    for i in range(m):
        for j in range(n):
            if X[i][j] == 'v' and X[(i + 1) % m][j] == '.':
                copy[(i + 1) % m][j] = 'v'
                copy[i][j] = '.'
                change2 = True
    X = [c[:] for c in copy]
    step += 1
    if not change1 and not change2:
        break

print(step)
