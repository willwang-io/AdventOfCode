def main():
    grid = []
    with open("test2.txt", "r") as f:
        lines = f.readlines()
    
    parse_moves = False
    moves = ''
    for line in lines:
        line = line.strip('\n')
        if not line:
            parse_moves = True
            continue
        if parse_moves:
            moves += line
        else:
            grid.append(list(line))

    walls = set()
    x, y = -1, -1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                x, y = i, j
            elif grid[i][j] == '#':
                walls.add((i, j))

    dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    
    for move in moves:
        print(move)
        dx, dy = dirs[move]
        xx, yy = x + dx, y + dy
        
        if (xx, yy) in walls:
            for row in grid:
                print(''.join(row))
            print()
            continue
        if grid[xx][yy] == '.':
            grid[xx][yy] = '@'
            grid[x][y] = '.'
            x, y = xx, yy
            for row in grid:
                print(''.join(row))
            print()
            continue
        cnt = 0
        while grid[xx][yy] == 'O':
            xx, yy = xx + dx, yy + dy
            cnt += 1
        if grid[xx][yy] == '#':
            for row in grid:
                print(''.join(row))
            print()
            continue
        if move == '>':
            for i in range(yy, y, -1):
                grid[xx][i] = grid[xx][i - 1]
            grid[xx][y] = '.'
            y += 1
        elif move == '<':
            for i in range(yy, y):
                grid[xx][i] = grid[xx][i + 1]
            grid[xx][yy] = '.'
            y -= 1
        elif move == '^':
            for i in range(xx, x, -1):
                grid[i][yy] = grid[i - 1][yy]
            grid[x][yy] = '.'
            x -= 1
        elif move == 'v':
            for i in range(xx, x, -1):
                grid[i][yy] = grid[i - 1][yy]
            grid[x][yy] = '.'
            x += 1
        for row in grid:
            print(''.join(row))
        print()




if __name__ == "__main__":
    main()