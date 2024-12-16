from collections import defaultdict
def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()
    d = defaultdict(int)
    d['b'] = 16076

    for _ in range(10000):
        for line in lines:
            line = line.strip()
            left, right = line.split(' -> ')
            if right == 'b':
                continue
            if 'AND' in left:
                a, b = left.split(' AND ')
                if a.isnumeric():
                    a = int(a)
                else:
                    if a in d:
                        a = d[a]
                    else:
                        continue
                if b.isnumeric():
                    b = int(b)
                else:
                    if b in d:
                        b = d[b]
                    else:
                        continue
                d[right] = a & b
            elif 'OR' in left:
                a, b = left.split(' OR ')
                if a.isnumeric():
                    a = int(a)
                else:
                    if a in d:
                        a = d[a]
                    else:
                        continue
                if b.isnumeric():
                    b = int(b)
                else:
                    if b in d:
                        b = d[b]
                    else:
                        continue    
                d[right] = a | b
            elif 'LSHIFT' in left:
                a, b = left.split(' LSHIFT ')
                if a.isnumeric():
                    a = int(a)
                else:
                    if a in d:
                        a = d[a]
                    else:
                        continue
                if b.isnumeric():
                    b = int(b)
                else:
                    if b in d:
                        b = d[b]
                    else:
                        continue
                d[right] = a << b
            elif 'RSHIFT' in left:
                a, b = left.split(' RSHIFT ')
                if a.isnumeric():
                    a = int(a)
                else:
                    if a in d:
                        a = d[a]
                    else:
                        continue
                if b.isnumeric():
                    b = int(b)
                else:
                    if b in d:
                        b = d[b]
                    else:
                        continue
                d[right] = a >> b
            elif 'NOT' in left:
                a = left.strip('NOT ')
                if a.isnumeric():
                    a = int(a)
                else:
                    if a in d:
                        a = d[a]
                    else:
                        continue
                d[right] = ~a & 0xFFFF
            else:
                if left in d:
                    d[right] = d[left]
                else:
                    if left.isnumeric():
                        d[right] = int(left)
                    else:
                        continue
    print(d['a'])

if __name__ == "__main__":
    main()


