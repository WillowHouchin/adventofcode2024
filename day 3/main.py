import re

def part1(data):
    data = re.findall('mul\(\w+,\w+\)', data)
    sum = 0
    for i in data:
        i = i.split(',')
        sum += int(i[0][4:]) * int(i[1][:-1])
    return sum

def part2(data):
    data = re.findall('mul\(\w+,\w+\)|do\(\)|don\'t\(\)', data)
    sum = 0
    mult = True
    for i in data:
        if i == 'do()': mult = True
        elif i == 'don\'t()': mult = False
        else:
            if not mult: continue
            i = i.split(',')
            sum += int(i[0][4:]) * int(i[1][:-1])
    return sum

if __name__=='__main__':
    # src = 'example.txt'
    src = 'data.txt'
    data = open(src, 'r').read()

    print(part1(data))
    print(part2(data))