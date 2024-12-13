N = 10000000000000
def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()
    lst = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        _, coord = line.split(': ')
        if '=' in line:
            cur = [int(i.split('=')[1]) + N for i in coord.split(', ')]
        else:
            cur = [int(i.split('+')[1]) for i in coord.split(', ')]

        lst.append((cur))
    ans = 0
    for i in range(0, len(lst), 3):
        ax, ay = lst[i]
        bx, by = lst[i + 1]
        px, py = lst[i + 2]
        
        det = ax * by - ay * bx
        if det == 0:
            continue
            
        x = (px * by - py * bx) // det
        y = (ax * py - px * ay) // det
        
        if x >= 0 and y >= 0:
            if ax * x + bx * y == px and ay * x + by * y == py:
                ans += x * 3 + y
    print(ans)



if __name__ == "__main__":
    main()