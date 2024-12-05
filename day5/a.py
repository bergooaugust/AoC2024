import regex as re

res = 0
with open('day5/a.input') as infile:
    
    match_regex = r'(\d+)\|(\d+)'
    
    res = 0
    manuals = []
    constraints = {}
    for line in infile:
        if re.match(match_regex, line):
            a, b = map(int, re.match(match_regex, line).groups())
            if b not in constraints.keys():
                constraints[b] = []
            constraints[b] += [a]
        elif len(line) > 1:
            manuals += [list(map(int, line.strip().split(',')))]
    for manual in manuals:
        legal = True
        for index, page in enumerate(manual):
            if page in constraints.keys():
                if any([constraint in manual[index:] for constraint in constraints[page]]):
                    legal = False
        if legal:
            res += manual[int(len(manual)/2)]


with open('day5/a.output', 'w') as outfile:
    outfile.write(str(res))