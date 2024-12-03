import numpy as np

res = 0
with open('day2/a.input') as infile:
    for line in infile:
        report = np.array([int(nbr) for nbr in line.strip().split()])
        safe = False
        for ignoreIndex in range(len(report)):
            report2 = np.append(report[0:ignoreIndex], report[ignoreIndex + 1:])
            diff = report2[1:] - report2[:-1]
            signs = np.sign(diff)
            if sum(signs) == len(signs) or sum(signs) == -len(signs):
                safe = True
                for nbr in diff * signs:
                    if nbr < 1 or nbr > 3:
                        safe = False
                        break
            if safe:
                break            
        if safe: 
            res += 1

with open('day2/b.output', 'w') as outfile:
    outfile.write(str(res))