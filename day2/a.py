import numpy as np

res = 0
with open('day2/a.input') as infile:
    for line in infile:
        report = np.array([int(nbr) for nbr in line.strip().split()])
        diff = report[1:] - report[:-1]
        signs = np.sign(diff)
        safe = False
        if sum(signs) == len(signs) or sum(signs) == -len(signs):
            safe = True
            for nbr in diff * signs:
                if nbr < 1 or nbr > 3:
                    safe = False
                    break
        if safe: 
            res += 1

with open('day2/a.output', 'w') as outfile:
    outfile.write(str(res))