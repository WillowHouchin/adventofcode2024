def findGuard(data):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in [ '<', '^', '>', 'v' ]:
                return y, x
    return -1, -1

def move(data, y, x):
    match(data[y][x]):
        case '<':
            if x == 0: return -1, -1
            if data[y][x-1] == '#':
                data[y][x] = '^'
            else:
                data[y][x-1] = '<'
                data[y][x] = 'X'
                x -= 1

        case '^':
            if y == 0: return -1, -1
            if data[y-1][x] == '#':
                data[y][x] = '>'
            else:
                data[y-1][x] = '^'
                data[y][x] = 'X'
                y -= 1

        case '>':
            if x == len(data[y]) - 1: return -1, -1
            if data[y][x+1] == '#':
                data[y][x] = 'v'
            else:
                data[y][x+1] = '>'
                data[y][x] = 'X'
                x += 1

        case 'v':
            if y == len(data) - 1: return -1, -1
            if data[y+1][x] == '#':
                data[y][x] = '<'
            else:
                data[y+1][x] = 'v'
                data[y][x] = 'X'
                y += 1
        
    return y, x

def part1(data):
    pos = findGuard(data)
    while -1 not in pos: pos = move(data, pos[0], pos[1])
    return sum(x.count('X') for x in data) + 1

def part2(data):
    pass

if __name__ == '__main__':
    # src = 'example.txt'
    src = 'data.txt'
    data = [ list(i) for i in open(src, 'r').read().split('\n') ]

    print(part1(data))