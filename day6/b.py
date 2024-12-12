import regex as re
import numpy as np
from tqdm import tqdm

res = 0
with open('day6/a.input') as infile:
    
    res = 0
    grid = np.array([list(line.strip()) for line in infile])
    start_obstacles = np.zeros(grid.shape)
    guard_start_pos = [0, 0]
    start_facing = '^'

    #setup
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '#':
                start_obstacles[y][x] = 1
            elif c != '.':
                guard_start_pos = [x, y]
                start_facing = c
    



    def on_grid(pos) -> bool:
        return pos[0] < grid.shape[0] and pos[1] < grid.shape[1] and pos[0] > -1 and pos[1] > -1

    def find_loop(obstacles2) -> bool:
        visited = [[[] for col in range(len(obstacles2))] for row in range(len(obstacles2))]

        guard_pos = guard_start_pos.copy()
        facing = start_facing

        while on_grid(guard_pos):
            if facing in visited[guard_pos[1]][guard_pos[0]]:
                return True
            else:
                visited[guard_pos[1]][guard_pos[0]] += [facing]

            match facing:
                case '^':
                    if not on_grid([guard_pos[0], guard_pos[1] - 1]) or obstacles2[guard_pos[1] - 1][guard_pos[0]] < 1:
                        guard_pos[1] -= 1
                    elif obstacles2[guard_pos[1] - 1][guard_pos[0]] > 0:
                        facing = '>'
                case '>':
                    if not on_grid([guard_pos[0] + 1, guard_pos[1]]) or obstacles2[guard_pos[1]][guard_pos[0] + 1] < 1:
                        guard_pos[0] += 1
                    elif obstacles2[guard_pos[1]][guard_pos[0] + 1] == 1:
                        facing = 'v'
                case 'v':
                    if not on_grid([guard_pos[0], guard_pos[1] + 1]) or obstacles2[guard_pos[1] + 1][guard_pos[0]] < 1:
                        guard_pos[1] += 1
                    elif obstacles2[guard_pos[1] + 1][guard_pos[0]] == 1:
                        facing = '<'
                case '<':
                    if not on_grid([guard_pos[0] - 1, guard_pos[1]]) or obstacles2[guard_pos[1]][guard_pos[0] - 1] < 1:
                        guard_pos[0] -= 1
                    elif obstacles2[guard_pos[1]][guard_pos[0] - 1] == 1:
                        facing = '^'
        return on_grid(guard_pos)
    
    for x in tqdm(range(len(grid))):
        for y in range(len(grid)):
            if start_obstacles[y][x] == 0 and guard_start_pos != [x, y]:
                test_obstacles = start_obstacles.copy()
                test_obstacles[y][x] = 1
                if find_loop(test_obstacles):
                    res += 1
    print(res)




with open('day6/b.output', 'w') as outfile:
    outfile.write(str(res))