import regex as re


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
    
    wrongs = []

    for manual in manuals:
        legal = True
        for index, page in enumerate(manual):
            if page in constraints.keys():
                if any([constraint in manual[index:] for constraint in constraints[page]]):
                    wrongs += [manual]
                    break

    corrects = []
    manual_index = 0

    while any(wrongs):
        
        manual_index %= len(wrongs)
        manual = wrongs[manual_index]

        if not manual:
            manual_index += 1
            continue
        
        for index, page in enumerate(manual):
            if page in constraints.keys():
                while any([constraint in manual[index:] for constraint in constraints[page]]):
                    temp = manual[index + 1]
                    manual[index + 1] = page
                    manual[index] = temp
                    break
        isSorted = True
        for index, page in enumerate(manual):
            if page in constraints.keys():
                if any([constraint in manual[index:] for constraint in constraints[page]]):
                    isSorted = False
                    wrongs[manual_index] = manual
        

        if isSorted:
            corrects += [manual]
            wrongs[manual_index] = False
            manual_index += 1
    for manual in corrects:
        res += manual[int(len(manual) / 2)]
                    
                        



with open('day5/b.output', 'w') as outfile:
    outfile.write(str(res))