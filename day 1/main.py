data = [ i.split('   ') for i in open('data.txt', 'r').read().split('\n') ]
left, right = [ [ i[0], i[1] ] for i in data ]

for i in data:
    left.append(int(i[0]))
    right.append(int(i[1]))

left.sort()
right.sort()

differences = []
similarities = []
for i in range(len(data)):
    differences.append(abs(right[i] - left[i]))
    if right[i] in left: similarities.append(right[i])

print(sum(differences))
print(sum(similarities))