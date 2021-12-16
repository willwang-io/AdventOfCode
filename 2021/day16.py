import math

versions = []


def solve(s):
    version, type_id, data = s[:3], s[3: 6], s[6:]
    versions.append(int(version, 2))

    if type_id == '100':
        i = 0
        ans = ''
        while True:
            ans += data[i + 1: i + 5]
            if data[i] == '0':
                break
            i += 5
        return int(ans, 2), s[i + 11:]
    else:
        sub_packets = []
        if data[0] == '0':
            length = int(data[1: 16], 2)
            nxt = data[16: 16 + length]
            rest = data[16 + length:]
            while nxt:
                a, nxt = solve(nxt)
                sub_packets.append(a)
        else:
            cnt = int(data[1: 12], 2)
            nxt = data[12:]
            for _ in range(cnt):
                a, nxt = solve(nxt)
                sub_packets.append(a)
            rest = nxt

        if type_id == '000':
            ans = sum(sub_packets)
        elif type_id == '001':
            ans = math.prod(sub_packets)
        elif type_id == '010':
            ans = min(sub_packets)
        elif type_id == '011':
            ans = max(sub_packets)
        elif type_id == '101':
            ans = sub_packets[0] > sub_packets[1]
        elif type_id == '110':
            ans = sub_packets[0] < sub_packets[1]
        else:
            ans = sub_packets[0] == sub_packets[1]
        return ans, rest


def main():
    file = open('input.txt', 'r')
    line = file.readline().strip()
    val = ''.join([bin(int(i, 16))[2:].zfill(4) for i in line])
    p2 = solve(val)[0]

    print(sum(versions))
    print(p2)


if __name__ == '__main__':
    main()
