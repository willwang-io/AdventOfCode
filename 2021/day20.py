import numpy as np
import scipy.signal


def convert(x):
    return 0 if x == '.' else 1


def solve(x, img, steps):
    ker = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])
    pad = 0
    for _ in range(steps):
        cur = np.pad(img, (2, 2), constant_values=pad)
        idx = scipy.signal.convolve2d(cur, ker, fillvalue=pad)
        img = np.array(x)[idx]
        pad = pad ^ 1
    print(np.sum(img))


def main():
    file = open('input.txt', 'r')
    x = list(map(convert, file.readline()))
    file.readline()
    img = []
    for line in file:
        cur = list(map(convert, line.strip()))
        img.append(cur)
    img = np.array(img)

    solve(x, img, 2)
    solve(x, img, 50)


if __name__ == '__main__':
    main()
