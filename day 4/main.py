# low key sucks tho but recursion funny
def search(data, x, y, letter=None, direction=None):
    found = 0
    if y > len(data) - 1 or y < 0: return 0
    if x > len(data[y]) - 1 or x < 0: return 0

    if letter != None:
        if "XMAS".find(data[y][x]) != "XMAS".find(letter) + 1: return 0
        if data[y][x] == 'S': return 1

    match(direction):
        case None:
            if data[y][x] != 'X': return 0
            letter = 'X'
            found += search(data, x-1, y+1, letter, 'upleft')
            found += search(data, x, y+1, letter, 'up')
            found += search(data, x+1, y+1, letter, 'upright')
            found += search(data, x-1, y, letter, 'left')
            found += search(data, x+1, y, letter, 'right')
            found += search(data, x-1, y-1, letter, 'downleft')
            found += search(data, x, y-1, letter, 'down')
            found += search(data, x+1, y-1, letter, 'downright')
        case 'upleft': found += search(data, x-1, y+1, data[y][x], direction)
        case 'up': found += search(data, x, y+1, data[y][x], direction)
        case 'upright': found += search(data, x+1, y+1, data[y][x], direction)
        case 'left': found += search(data, x-1, y, data[y][x], direction)
        case 'right': found += search(data, x+1, y, data[y][x], direction)
        case 'downleft': found += search(data, x-1, y-1, data[y][x], direction)
        case 'down': found += search(data, x, y-1, data[y][x], direction)
        case 'downright': found += search(data, x+1, y-1, data[y][x], direction)
    return found

def part1(data):
    found = 0
    for y in range(len(data)):
        for x in range(len(data)):
            found += search(data, x, y)
    return found


def part2(data):
    found = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data) - 1):
            if data[y][x] != 'A': continue
            # crude but effective
            if not ((data[y-1][x-1] == 'M' and data[y+1][x+1] == 'S') or (data[y-1][x-1] == 'S' and data[y+1][x+1] == 'M')): continue
            if not ((data[y+1][x-1] == 'M' and data[y-1][x+1] == 'S') or (data[y+1][x-1] == 'S' and data[y-1][x+1] == 'M')): continue
            found += 1
    return found

if __name__=='__main__':
    # src = 'example.txt'
    src = 'data.txt'
    data = open(src, 'r').read().split('\n')

    print(part1(data))
    print(part2(data))