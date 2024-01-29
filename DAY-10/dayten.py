lines=[]
with open('inputfile.txt', 'r') as f:
    for line in f:
        lines.append(line.rstrip())

pipes = {
        "|": ["N","S"],
        "-": ["W","E"],
        "L": ["N","E"],
        "J": ["W","N"],
        "7": ["W","S"],
        "F": ["S","E"]
    }

directions = {
        "N": [-1,0],
        "S": [1,0],
        "W": [0,-1],
        "E": [0,1],
    }

opposite_direction = {
        "N": "S",
        "S": "N",
        "W": "E",
        "E": "W",
    }

grid = [[cell for cell in line] for line in lines]
grid_steps = [[-1 for _ in line] for line in lines]
import sys
sys.setrecursionlimit(len(grid)*len(grid[0])*2)
arr=[]
for i in range(len(grid)):
    if 'S' in grid[i]:
        arr.append(i)
start_x=arr[0]
arr=[]
for i in range(len(grid[start_x])):
    if 'S' in grid[start_x][i]:
        arr.append(i)
start_y=arr[0]

valid_directions = []
for direction, value in directions.items():
    current_x = start_x + value[0]
    current_y = start_y + value[1]
    if current_x >= 0 and current_x < len(grid) and current_y >= 0 and current_y < len(grid[0]):
        if grid[current_x][current_y] == '.':
            continue
        if opposite_direction[direction] in pipes[grid[current_x][current_y]]:
            valid_directions.append(direction)

for key in pipes.keys():
    if valid_directions[0] in pipes[key] and valid_directions[1] in pipes[key]:
        grid[start_x][start_y] = key
        break
current_path=[]
def func(current_location, current_path):
        valid_directions = pipes[grid[current_location[0]][current_location[1]]]
        
        for direction in valid_directions:
            new_path = list(current_path)
            x, y = directions[direction]
            x += current_location[0]
            y += current_location[1]
            
            if [x,y] in new_path:
                continue
            
            if grid_steps[x][y] == -1 or grid_steps[x][y] > len(new_path):
                loc = [x,y]
                new_path.append(loc)
                grid_steps[x][y] = len(new_path)
                func(loc, new_path)
                continue

func([start_x, start_y],[])
ans1=-1
for l in grid_steps:
    for c in l:
        if c>ans1:
            ans1=c
print("Part 1:",ans1)

