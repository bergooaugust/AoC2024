import regex as re
import numpy as np

res = 0
with open('day4/a.input') as infile:
    
    match_regex = r'SAM|MAS'
    
    res = 0
    chars = []
    for line in infile:
        chars.append(list(line.strip()))
    chars = np.array(chars)

    for x in range(chars.shape[0] - 2):
        for y in range(chars.shape[1] - 2):
            sub_matrix = chars[x:x+3,y:y+3]
            if re.match(match_regex, ''.join(sub_matrix.diagonal())) and re.match(match_regex, ''.join(np.fliplr(sub_matrix).diagonal())):
                res += 1



with open('day4/b.output', 'w') as outfile:
    outfile.write(str(res))