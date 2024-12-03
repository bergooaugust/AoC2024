import numpy as np

with open('day1/a.input') as infile:
    a = []
    b = []
    for line in infile:
        pair = line.strip().split()
        a += [int(pair[0])]
        b += [int(pair[1])]

    a.sort()
    b.sort()
    diff = np.array(a) - np.array(b)
    res = np.sum(diff * np.sign(diff))
    open('day1/a.output', 'w').write(str(res))