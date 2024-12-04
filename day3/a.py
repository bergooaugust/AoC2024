import regex as re

res = 0
with open('day3/a.input') as infile:
    
    match_regex = r'mul\(([0-9]+),([0-9]+)\)'
    
    res = 0
    for line in infile:
        matches = re.findall(match_regex, line)
        for match in matches:
            a = int(match[0])
            b = int(match[1])
            res += a * b

with open('day3/a.output', 'w') as outfile:
    outfile.write(str(res))