import regex as re
import numpy as np

res = 0
with open('day4/a.input') as infile:
    
    match_regex = r'(?=XMAS)|(?=SAMX)'
    
    res = 0
    chars = []
    for line in infile:
        chars.append(list(line.strip()))
    chars = np.array(chars)

    #horizontal
    res += sum([len(re.findall(match_regex, ''.join(line))) for line in chars])

    #vertical
    res += sum([len(re.findall(match_regex, ''.join(line))) for line in chars.transpose()])
    
    
    #diagonals
    diags_1 = [chars.diagonal(offset=k) for k in range(-chars.shape[0], chars.shape[1])]
    diags_2 = [np.fliplr(chars).diagonal(offset=k,) for k in range(-chars.shape[1], chars.shape[0])]

    res += sum([len(re.findall(match_regex, ''.join(line))) for line in diags_1])
    res += sum([len(re.findall(match_regex, ''.join(line))) for line in diags_2])


with open('day4/a.output', 'w') as outfile:
    outfile.write(str(res))