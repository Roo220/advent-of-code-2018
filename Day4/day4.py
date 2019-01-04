import random

class Guard:
    id = ''
    days = []

class Day:
    id = ''
    minutes = []
    sleep = 0

with open('data') as f:
    data = f.read().splitlines()

data = sorted(data)
guards = []

# GET A LIST OF THE GUARDS
# for d in data:
#     # print d
#     dateTime = d.split('[')[1].split(']')[0]
#     date = dateTime.split(' ')[0]
#     message = d.split(']')[1]
#     g = Guard()
#
#     if message.split(' ')[1] == 'Guard':
#         id = message.split('#')[1].split(' ')[0]
#         if any(x for x in guards if x.id == id):
#             g = [x for x in guards if x.id == id][0]
#         else:
#             g.id = id
#             guards.append(g)

days = []
day = None
# ADD A LIST OF DAYS TO THE GUARDS
for d in data:
    dateTime = d.split('[')[1].split(']')[0]
    hour = dateTime.split(' ')[1].split(':')[0]
    minutes = int(dateTime.split(':')[1])
    id = ''
    message = d.split(']')[1]

    if message.split(' ')[1] == 'Guard':
        if day is not None:
            day.sleep = day.minutes.count('#')
            days.append(day)
        day = Day()
        day.id = message.split('#')[1].split(' ')[0]
        day.minutes = ['.'] * 60
    else:
        if 'falls' in message:
            day.minutes[minutes:59] = ['#'] * (59 - minutes)
        elif 'wakes' in message:
            day.minutes[minutes:59] = ['.'] * (59 - minutes)
        else:
            print 'error'

day.sleep = day.minutes.count('#')
days.append(day)

# print len(days[0].minutes)
# print len(days[1].minutes)
# print len(days[2].minutes)
# print len(days[3].minutes)

sleepyDay = max(days, key=lambda day: day.sleep)

print sleepyDay.id

guard277 = filter(lambda day: day.id == '277', days)
print len(guard277)
# for i in guard277:
#     print i.minutes[19:]

guards = {}
for d in days:
    if d.id in guards:
        guards[d.id] = int(guards.get(d.id)) + int(d.sleep)
    else:
        guards[d.id] = int(d.sleep)

# for x, y in guards.items():
    # print "{}: {}".format(x, y)

print "max(guards) = {}".format(max(guards))
maxGuards = max(guards, key=guards.get)
print "max(guards, key=guards.get()) = {}".format(maxGuards)
# print "guards[maxGuards] = {}".format(guards['421'])

# guard2591 = filter(lambda day: day.id == '421', days)

# print len(guard2591)

# mins = []
# for i in range(60):
#     totalMin = 0
#     for j in guard2591:
#         if j.minutes[i] == '#':
#             totalMin += 1
#     mins.append(totalMin)
#
# print mins[0:]
# for i in guard2591:
#     print i.minutes[26:]

guardDays = {}

for d in days:
    if d.id in guardDays:
        guardDays[d.id].append(d.minutes)
    else:
        guardDays[d.id] = [d.minutes]

for i, j in guardDays.items():
    print i

    mins = []

    for x in range(60):
        totalMin = 0
        for y in j:
            if y[x] == '#':
                totalMin += 1
        mins.append(totalMin)

    print mins[0:]

# for g in guards:
#     mins = []
#     for i in range(60):
#         totalMin = 0
#         for j in d.minutes:
#             if j == '#':
#                 totalMin += 1
#         mins.append(totalMin)
#     guardMins[d.id] = totalMin
#
# print guardMins


