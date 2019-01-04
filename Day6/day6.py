with open('data') as f:
    data = f.read().splitlines()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao',
            'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax']

world_map = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

# world_map = [['.'] * 10] * 10
#
world_map = []
for i in range(400):
    world_map.append(['.'] * 400)

coordinates = {}

for d in range(len(data)):
    coordinates[alphabet[d]] = data[d]

for i, j in coordinates.items():
    x = int(j.split(',')[0])
    y = int(j.split(', ')[1])

    # print j
    world_map[x][y] = i.upper()


area_under_value = 0

print ""
for i in range(len(world_map)):
    for j in range(len(world_map)):
        manhat = {}
        manhat_safe = 0
        for k, v in coordinates.items():
            x = int(v.split(',')[0])
            y = int(v.split(', ')[1])
            distance = abs(i - x) + abs(j - y)

            if world_map[i][j] == '.':
                manhat[k] = distance
            manhat_safe += distance

        if manhat_safe < 10000:
            area_under_value += 1

        if len(manhat) > 0:
            min_dist_value = min(manhat.values())
            if manhat.values().count(min_dist_value) == 1:
                minDist = min(manhat, key=manhat.get)
                world_map[i][j] = minDist

for y in world_map:
    print y
print ""
d_count = sum([i.count('d') for i in world_map])
D_count = sum([i.count('D') for i in world_map])

print d_count + D_count

finite_letters = alphabet
edge = world_map[0][0:] + [i[-1] for i in world_map[1:-1]] + world_map[-1][0:] + [i[0] for i in world_map[1:-1]]

print "top edge: {}".format(world_map[0][0:])
print "right edge: {}".format([i[-1] for i in world_map[1:-1]])
print "bottom edge: {}".format(world_map[-1][0:])
print "left edge: {}".format([i[0] for i in world_map[1:-1]])

print edge
print len(edge)

for a in alphabet:

    if a in edge:
        finite_letters = filter(lambda x: x != a, finite_letters)

print finite_letters

ans = {}
for f in finite_letters:
    print f
    print sum([i.count(f) for i in world_map])
    ans[f] = sum([i.count(f) for i in world_map]) + 1

print ans
print max(ans.values())

print area_under_value

# for i in world_map:
#     print i
# for i in large_world_map:
#     print i