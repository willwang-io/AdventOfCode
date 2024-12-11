from collections import defaultdict

def transform_number(i, memo):
    if i in memo:
        return memo[i]
    
    if i == 0:
        result = {1: 1}
    else:
        num = i
        digits = 0
        while num:
            num = num // 10
            digits += 1
        if digits % 2 == 0:
            half = digits // 2
            left = i // (10 ** half)
            right = i % (10 ** half)
            result = defaultdict(int)
            result[left] += 1
            result[right] += 1
        else:
            result = {i * 2024: 1}
    
    memo[i] = result
    return result

def main():
    with open("in.txt", "r") as f:
        numbers = map(int, f.readline().split())
    
    freq = defaultdict(int)
    for num in numbers:
        freq[num] += 1
    
    memo = {}
    for k in range(75):
        new_freq = defaultdict(int)
        for num, count in freq.items():
            transformed = transform_number(num, memo)
            for t_num, t_count in transformed.items():
                new_freq[t_num] += count * t_count
        freq = new_freq
        total = sum(freq.values())
        print(k, total)
    
    print(sum(freq.values()))

if __name__ == "__main__":
    main()