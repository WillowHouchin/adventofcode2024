def findAntenna(data):
    antenna = []
    for y, yv in enumerate(data):
        for x, xv in enumerate(yv):
            if xv != '.': antenna.append([ xv, y, x ])
    return sorted(antenna)

def part1(data):
    antenna = findAntenna(data)
    for y, yv in enumerate(data):
        for x in range(len(yv)):
            for a1 in antenna:
                for a2 in antenna:
                    if a1 == a2: continue
                    if a1[0] != a2[0]: continue
                    distance1 = [ y - a1[1], x - a1[2] ]
                    distance2 = [ a1[1] - a2[1], a1[2] - a2[2] ]
                    if distance1[0] == distance2[0] and distance1[1] == distance2[1]: data[y][x] = '#'
    return sum(i.count('#') for i in data)

def part2(data):
    antenna = findAntenna(data)
    for y, yv in enumerate(data):
        for x in range(len(yv)):
            for a1 in antenna:
                for a2 in antenna:
                    if a1 == a2: continue
                    if a1[0] != a2[0]: continue
                    slope1 = 'inf' if x - a1[2] == 0 else (y - a1[1]) / (x - a1[2])
                    slope2 = 'inf' if a1[2] - a2[2] == 0 else (a1[1] - a2[1]) / (a1[2] - a2[2])
                    if slope1 == slope2: data[y][x] = '#'
    return sum(i.count('#') for i in data)

if __name__ == '__main__':
    # src = 'example.txt'
    src = 'data.txt'
    data = [ list(i) for i in open(src, 'r').read().split('\n') ]

    # both are slow but do work
    print(part1(data))
    print(part2(data))