def solve(lst, program):
    d = {'A': lst[0], 'B': lst[1], 'C': lst[2]}
    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: d['A'], 5: d['B'], 6: d['C']}
    i = 0
    ans = []
    while i < len(program):
        cur, val = program[i], program[i + 1]
        if cur == 0:
            d['A'] = d['A'] // (2 ** combo[val]) 
            combo[4] = d['A']
        elif cur == 1:
            d['B'] = d['B'] ^ val
            combo[5] = d['B']
        elif cur == 2:
            d['B'] = combo[val] % 8
            combo[5] = d['B']
        elif cur == 3:
            if d['A'] == 0:
                i += 2
                continue
            if val != i:
                i = val
                continue
        elif cur == 4:
            d['B'] = d['B'] ^ d['C']
            combo[5] = d['B']
        elif cur == 5:
            ans.append(combo[val] % 8)
            if ans != program[:len(ans)]:
                return False
        elif cur == 6:
            d['B'] = d['A'] // (2 ** combo[val]) 
            combo[5] = d['B']
        elif cur == 7:
            d['C'] = d['A'] // (2 ** combo[val]) 
            combo[6] = d['C']
        i += 2
    return ans == program

def main():
    test_lst = [729, 0, 0]
    test_program = [0,1,5,4,3,0]

    actual = [44348299, 0, 0]
    actual_program = [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]
    tests = [
        # ((0, 0, 9), [2, 6]),
        # ((10, 0, 0), [5,0,5,1,5,4]),
        # ((2024, 0, 0), [0,1,5,4,3,0])
        ((117440, 0, 0), [0,3,5,4,3,0]),
        # ((44348299, 0, 0), [2,4,1,5,7,5,1,6,0,3,4,2,5,5,3,0]),
    ]
    for A in range(100000000, 1000000000):
        if A % 1000000 == 0:
            print(A)
        if solve((A, 0, 0), actual_program):
            print(A)
            break

if __name__ == '__main__':
    main()