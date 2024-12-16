import itertools
x = "1113122113"
for i in range(50):
    x = ''.join(str(len(list(g)))+k for k, g in itertools.groupby(x))
print(len(x))
