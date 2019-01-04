with open('data') as f:
    data = f.read()

originalData = data
changed = True

stringLength = len(data)

print data


while changed:

    changed = False
    stringLength = len(data)

    # print data[13]
    # print stringLength
    for i in range(stringLength - 1):
        try:
            if data[i] == data[(i + 1)].swapcase():
                changed = True
                data = data[:i] + data[(i+2):]
        except:
            errors = ""

lengths = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
print "string test"
print originalData.strip('a')

for letter in alphabet:
    print letter
    data = originalData
    data = data.replace(letter, "")
    data = data.replace(letter.upper(), "")
    changed = True
    print data

    while changed:

        changed = False
        stringLength = len(data)

        # print data[13]
        # print stringLength
        for i in range(stringLength - 1):
            try:
                if data[i] == data[(i + 1)].swapcase():
                    changed = True
                    data = data[:i] + data[(i + 2):]
            except:

                errors = ""
    lengths.append(len(data))

print lengths[0:]
print min(lengths)