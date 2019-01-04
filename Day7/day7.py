with open('data') as f:
    data = f.read().splitlines()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F']

# take all steps without any before, sort and add to the list
# fina all the steps with preqs met, sort and add to the list

steps_after = {}
steps_before = {}
sorted_list = []
for a in alphabet:
    steps_before[a] = []
    steps_after[a] = []

for d in data:
    first_step = d.split(' ')[1]
    sec_step = d.split(' ')[7]
    steps_before[sec_step].append(first_step)
    steps_after[first_step].append(sec_step)
print steps_before
print steps_after

sorted_list = []
while len(sorted_list) != 26:
    next_steps = sorted({x: v for x, v in steps_before.items() if set(v).issubset(sorted_list)}.keys())
    next_steps = [x for x in next_steps if x not in sorted_list][0]
    print next_steps
    sorted_list += next_steps

print sorted_list

