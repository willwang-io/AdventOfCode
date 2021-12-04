def bingo(board):
    x = [board[i:i+5] for i in range(0, len(board), 5)]
    y = list(zip(*x))
    return any(sum(i) == 0 for i in x) or any(sum(j) == 0 for j in y)


def part1(nums, boards):
    boards = [boards[i:i+25] for i in range(0, len(boards), 25)]
    for num in nums:
        for i in range(len(boards)):
            boards[i] = [x if x != num else -1 for x in boards[i]]
            if bingo(boards[i]):
                print(num * sum(boards[i]))
                return


def part2(nums, boards):
    boards = [boards[i:i+25] for i in range(0, len(boards), 25)]
    win = [False] * len(boards)
    ans = 0
    for num in nums:
        for i in range(len(boards)):
            if win[i]:
                continue
            boards[i] = [x if x != num else 0 for x in boards[i]]
            if bingo(boards[i]):
                win[i] = True
                ans = num * sum(boards[i])
    print(ans)


def main():
    lst = ""
    with open('input.txt') as file:
        for line in file:
            lst += line
    lst = lst.split()
    nums, boards = list(map(int, lst[0].split(','))), list(map(int, lst[1:]))
    part1(nums, boards)
    part2(nums, boards)


if __name__ == '__main__':
    main()
