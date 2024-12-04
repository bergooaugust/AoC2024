import regex as re

res = 0
with open('day3/a.input') as infile:
    
    match_regex = r'mul\(([0-9]+),([0-9]+)\)'

    do_regex = r'do\(\)'

    dont_regex = r'don\'t\(\)'
    
    res = 0
    
    all_text = ""

    doing = True
    dos = []
    for line in infile:
        while len(line) > 0:
            if doing:
                match = re.search(dont_regex, line)
                if match == None:
                    dos += [line]
                    break
                dos += [line[:match.end()]]
                line = line[match.end():]
                doing = False
            else:
                match = re.search(do_regex, line)
                if match == None:
                    break
                line = line[match.end():]
                doing = True

    for do in dos:
        matches = re.findall(match_regex, do)
        for match in matches:
            a = int(match[0])
            b = int(match[1])
            res += a * b

with open('day3/b.output', 'w') as outfile:
    outfile.write(str(res))