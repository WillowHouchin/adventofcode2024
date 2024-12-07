operator_dict = {
    '+': lambda x, y: x + y, # add
    '-': lambda x, y: x - y, # subtract
    '*': lambda x, y: x * y, # multiply
    '/': lambda x, y: x // y if x % y == 0 else 'stop', # integer division
    '||': lambda x, y: int(str(x) + str(y)), # concatenate
    '&&': lambda x, y: int(str(x)[:-len(str(y))]) if len(str(abs(x))) > len(str(y)) and str(x)[len(str(x))-len(str(y)):] == str(y) else 'stop' # unconcatenate?
}

opposite = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*',
    '||': '&&',
    '&&': '||'
}

def check(target, nums, operator):
    if target == 'stop': return 0
    if len(nums) == 1: return target == nums[0]
    for v in operator:
        if check(operator_dict[opposite[v]](target, nums[-1]), nums[:-1], operator) != 0: return target
    return 0

if __name__ == '__main__':
    # src = 'example.txt'
    # src = 'test.txt'
    src = 'data.txt'
    data = open(src, 'r').read().replace(':', '').split('\n')
    for i in range(len(data)): data[i] = [ int(j) for j in data[i].split(' ') ]

    print(sum(check(line[0], line[1:], ('+', '*')) for line in data)) # part 1
    print(sum(check(line[0], line[1:], ('+', '*', '||')) for line in data)) # part 2