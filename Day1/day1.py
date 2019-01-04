import json 

with open('data.json') as f:
    data = json.load(f)

print("total: {0}".format(sum(map(int, data["data"]))))

freqs = []
freq = 0
result = 0

while result == 0:
    for it in map(int, data["data"]):
        # print "freq: {0} + {1} equals {2}".format(freq, it, freq + it)
        freq = freq + it

        if freq in freqs:
            print freq
            result = freq

        freqs.append(freq)
    print("Round again")

print(result)
