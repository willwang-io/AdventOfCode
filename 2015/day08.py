from collections import defaultdict
def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()

    x = 0
    y = 0
    for line in lines:
        line = line.strip()
        x += len(line)
        line = line.replace("\\", "\\\\")
        line = line.replace("\"", '\\"')
        y += len(line) + 2
    print(x, y)
    print(y - x)


if __name__ == "__main__":
    main()
