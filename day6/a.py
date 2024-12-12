import regex as re
import numpy as np

res = 0
with open('day6/a.input') as infile:
    
    res = 0
    grid = np.array([list(line.strip()) for line in infile])
    print(grid.shape)
    obstacles = np.zeros(grid.shape)
    guard_pos = [0, 0]
    facing = '^'

    #setup
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '#':
                obstacles[y][x] = 1
            elif c != '.':
                guard_pos = [x, y]
                facing = c
    print(obstacles)
    
    visited = np.zeros(grid.shape)

    def on_grid(pos) -> bool:
        return pos[0] < grid.shape[0] and pos[1] < grid.shape[1] and pos[0] > -1 and pos[1] > -1

    while on_grid(guard_pos):
        visited[guard_pos[1]][guard_pos[0]] = 1
        match facing:
            case '^':
                if not on_grid([guard_pos[0], guard_pos[1] - 1]) or obstacles[guard_pos[1] - 1][guard_pos[0]] < 1:
                    guard_pos[1] -= 1
                elif obstacles[guard_pos[1] - 1][guard_pos[0]] > 0:
                    facing = '>'
                    guard_pos[0] += 1
            case '>':
                if not on_grid([guard_pos[0] + 1, guard_pos[1]]) or obstacles[guard_pos[1]][guard_pos[0] + 1] < 1:
                    guard_pos[0] += 1
                elif obstacles[guard_pos[1]][guard_pos[0] + 1] == 1:
                    facing = 'v'
                    guard_pos[1] += 1
            case 'v':
                if not on_grid([guard_pos[0], guard_pos[1] + 1]) or obstacles[guard_pos[1] + 1][guard_pos[0]] < 1:
                    guard_pos[1] += 1
                elif obstacles[guard_pos[1] + 1][guard_pos[0]] == 1:
                    facing = '<'
                    guard_pos[0] -= 1
            case '<':
                if not on_grid([guard_pos[0] - 1, guard_pos[1]]) or obstacles[guard_pos[1]][guard_pos[0] - 1] < 1:
                    guard_pos[0] -= 1
                elif obstacles[guard_pos[1]][guard_pos[0] - 1] == 1:
                    facing = '^'
                    guard_pos[1] -= 1
    
    res = sum([sum(row) for row in visited])
        



with open('day6/a.output', 'w') as outfile:
    outfile.write(str(res))