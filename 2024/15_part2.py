def main():
    grid = []
    with open("in.txt", "r") as f:
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
            expanded_line = ''
            for c in line:
                if c == 'O':
                    expanded_line += '[]'
                elif c == '.':
                    expanded_line += '..'
                elif c == '#':
                    expanded_line += '##'
                else:
                    expanded_line += c + '.'
            grid.append(list(expanded_line))
    walls = set()
    x, y = -1, -1

    for i in range(len(grid)):
        # print(''.join(grid[i]))
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                x, y = i, j
            elif grid[i][j] == '#':
                walls.add((i, j))

    dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    
    for move in moves:
        if move == 'v' and x == 2 and y == 11:
            whatever = 'whatever'
        dx, dy = dirs[move]
        xx, yy = x + dx, y + dy
        
        if (xx, yy) in walls:
            continue
        if grid[xx][yy] == '.':
            grid[xx][yy] = '@'
            grid[x][y] = '.'
            x, y = xx, yy
            continue
        cnt = 0
        layers = []
        ok = True
        if move == '>' or move == '<':
            while grid[xx][yy] == '[' or grid[xx][yy] == ']':
                xx, yy = xx + dx, yy + dy
                cnt += 1
        else:
            if grid[xx][yy] == ']':
                layers.append([(xx, yy - 1, xx, yy)])
            if grid[xx][yy] == '[':
                layers.append([(xx, yy, xx, yy + 1)])
            if move == '^':
                for _ in range(200):
                    cur_layer = []
                    for fx, y1, _, y2 in layers[-1]:
                        if grid[fx - 1][y1] == '#' or grid[fx - 1][y2] == '#':
                            ok = False
                            break
                        if grid[fx - 1][y1] == ']':
                            cur_layer.append((fx - 1, y1 - 1, fx - 1, y1))
                        if grid[fx - 1][y1] == '[':
                            cur_layer.append((fx - 1, y1, fx - 1, y1 + 1))
                        if grid[fx - 1][y2] == ']':
                            cur_layer.append((fx - 1, y2 - 1, fx - 1, y2))
                        if grid[fx - 1][y2] == '[':
                            cur_layer.append((fx - 1, y2, fx - 1, y2 + 1))
                    if not ok or len(cur_layer) == 0:
                        break
                    layers.append(set(cur_layer))
            elif move == 'v':
                for _ in range(200):
                    cur_layer = []
                    for fx, y1, _, y2 in layers[-1]:
                        if grid[fx + 1][y1] == '#' or grid[fx + 1][y2] == '#':
                            ok = False
                            break
                        if grid[fx + 1][y1] == ']':
                            cur_layer.append((fx + 1, y1 - 1, fx + 1, y1))
                        if grid[fx + 1][y1] == '[':
                            cur_layer.append((fx + 1, y1, fx + 1, y1 + 1))
                        if grid[fx + 1][y2] == ']':
                            cur_layer.append((fx + 1, y2 - 1, fx + 1, y2))
                        if grid[fx + 1][y2] == '[':
                            cur_layer.append((fx + 1, y2, fx + 1, y2 + 1))
                    if not ok or len(cur_layer) == 0:
                        break
                    layers.append(set(cur_layer))

        if grid[xx][yy] == '#' or not ok:
            continue

        if move == '>':
            for i in range(yy, y, -1):
                grid[xx][i] = grid[xx][i - 1]
            grid[xx][y] = '.'
            y += 1
        elif move == '<':
            for i in range(yy, y):
                grid[xx][i] = grid[xx][i + 1]
            grid[xx][y] = '.'
            y -= 1
        elif move == '^':
            for layer in layers[::-1]:
                for x1, y1, x2, y2 in layer:
                    grid[x1 - 1][y1] = '['
                    grid[x2 - 1][y2] = ']'
                    grid[x1][y1] = '.'
                    grid[x2][y2] = '.'
            grid[x][y] = '.'
            x -= 1
            grid[x][y] = '@'
        elif move == 'v':
            for layer in layers[::-1]:
                for x1, y1, x2, y2 in layer:
                    grid[x1 + 1][y1] = '['
                    grid[x2 + 1][y2] = ']'
                    grid[x1][y1] = '.'
                    grid[x2][y2] = '.'
            grid[x][y] = '.'
            x += 1
            grid[x][y] = '@'
    
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '[':
                ans += i * 100 + j
    print(ans)


if __name__ == "__main__":
    main()