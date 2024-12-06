from functools import cmp_to_key

def checkUpdate(orders, update):
    for order in orders:
        if (order[0] in update and order[1] in update) and (update.index(order[0]) > update.index(order[1])): return False
    return True

def compareOrder(page1, page2): # probably slow 
    for order in orders:
        if page1 in order and page2 in order:
            return -1 if page1 == order[0] else 1
    return 0

# def updateKey(page): # solid estimate but not accurate
#     sum = 0
#     for order in orders:
#         if order[0] == page: sum += 1
#         if order[1] == page: sum -= 1
    # return sum

def fixUpdate(orders, update):
    update = sorted(update, key=cmp_to_key(compareOrder)) # not a huge fan of cmp_to_key but it definitely works
    # update = sorted(update, key=updateKey)
    return update

def part1(orders, updates):
    # sum = 0
    # for update in updates:
    #     if checkUpdate(orders, update): sum += update[len(update)//2]
    # return sum
    return sum(update[len(update)//2] for update in updates if checkUpdate(orders, update))

def part2(orders, updates):
    # sum = 0
    # for update in updates:
    #     if not checkUpdate(orders, update): sum += fixUpdate(orders, update)[len(update)//2]
    # return sum
    return sum(fixUpdate(orders, update)[len(update)//2] for update in updates if not checkUpdate(orders, update))

if __name__ == '__main__':
    # src = 'example.txt'
    src = 'data.txt'
    data = open(src, 'r').read().split('\n\n')
    orders = [ i.split('|') for i in data[0].split('\n') ]
    updates = [ i.split(',') for i in data[1].split('\n') ]
    
    for i in range(len(orders)): orders[i] = [ int(j) for j in orders[i] ]
    for i in range(len(updates)): updates[i] = [ int(j) for j in updates[i] ]

    print(part1(orders, updates))
    print(part2(orders, updates))