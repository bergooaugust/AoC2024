import numpy as np

with open('day1/a.input') as infile:
    a = []
    b = []
    for line in infile:
        pair = line.strip().split()
        a += [int(pair[0])]
        b += [int(pair[1])]
    freqs = {}

    res = 0
    for key in a:
        if key not in freqs.keys():
            freqs[key] = b.count(key)

        res += key * freqs[key]

    open('day1/b.output', 'w').write(str(res))