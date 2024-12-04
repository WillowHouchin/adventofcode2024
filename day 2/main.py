# this solution sucks
def check(line):
    safe = True
    mode = ''
    last = line[0]
    for k, j in enumerate(line):
        if k == 0: continue
        if j - last >= 1 and j - last <= 3:
            if mode == 'decreasing': return False
            mode = 'increasing'
        elif last - j >= 1 and last - j <= 3:
            if mode == 'increasing': return False
            mode = 'decreasing'
        else: return False
        last = j
    return True


def part1(data):
    safe_reports = 0
    for i in data:
        if check(i): safe_reports += 1
    return safe_reports

# this solution is ok ig
def part2(data):
    safe_reports = 0
    for i in data:
        if check(i): safe_reports += 1
        else:
            # this is dumb but necessary
            for j in range(len(i)):
                temp = i[:]
                temp.pop(j)
                if check(temp):
                    safe_reports += 1
                    break
    return safe_reports

if __name__ == '__main__':
    # data = [ i.split() for i in open('example.txt', 'r').read().split('\n') ]
    data = [ i.split() for i in open('data.txt', 'r').read().split('\n') ]

    for i in range(len(data)): data[i] = [ int(j) for j in data[i] ]

    print(part1(data))
    print(part2(data))