# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# First we will need access to the full file in array form.
global maze 
maze = []

# Defining functions.
def find_first_two_pipes(coordinates): # To check which two pipes are valid from the start point.
    pipes = []
    if maze[coordinates[0] - 1][coordinates[1]] in ["|", "7", "F"]: # Checks if connected to above pipe.
        pipes.append([coordinates[0] - 1, coordinates[1]])
        if len(pipes) == 2:
            return pipes
    
    if maze[coordinates[0]][coordinates[1] - 1] in ["-", "L", "F"]: # Checks if connected to left pipe.
        pipes.append([coordinates[0], coordinates[1] - 1])
        if len(pipes) == 2:
            return pipes
        
    if maze[coordinates[0]][coordinates[1] + 1] in ["-", "J", "7"]: # Checks if connected to right pipe.
        pipes.append([coordinates[0], coordinates[1] + 1])
        if len(pipes) == 2:
            return pipes
        
    if maze[coordinates[0] + 1][coordinates[1]] in ["|", "J", "L"]: # Checks if connected to below pipe.
        pipes.append([coordinates[0] + 1, coordinates[1]])
        if len(pipes) == 2:
            return pipes

def find_next_position_to_check(coordinates, side):
    pipe = maze[coordinates[0]][coordinates[1]]

    match pipe:
        case "|":
            if [coordinates[0] - 1, coordinates[1]] in coordinates_checked[side]: # Just come from the top.
                return [coordinates[0] + 1, coordinates[1]] # down
            
            else:
                return [coordinates[0] - 1, coordinates[1]] # up
            
        case "-":
            if [coordinates[0], coordinates[1] - 1] in coordinates_checked[side]: # Just come from the left.
                return [coordinates[0], coordinates[1] + 1] # right
            
            else:
                return [coordinates[0], coordinates[1] - 1] # left
        
        case "L":
            if [coordinates[0] - 1, coordinates[1]] in coordinates_checked[side]: # Just come from the top.
                return [coordinates[0], coordinates[1] + 1] # right
            
            else:
                return [coordinates[0] - 1, coordinates[1]] # up
            
        case "J":
            if [coordinates[0] - 1, coordinates[1]] in coordinates_checked[side]: # Just come from the top.
                return [coordinates[0], coordinates[1] - 1] # left
            
            else:
                return [coordinates[0] - 1, coordinates[1]] # up
            
        case "7":
            if [coordinates[0], coordinates[1] - 1] in coordinates_checked[side]: # Just come from the left.
                return [coordinates[0] + 1, coordinates[1]] # down
            
            else:
                return [coordinates[0], coordinates[1] - 1] # left
            
        case "F":
            if [coordinates[0], coordinates[1] + 1] in coordinates_checked[side]: # Just come from the right.
                return [coordinates[0] + 1, coordinates[1]] # down
            
            else:
                return [coordinates[0], coordinates[1] + 1] # right
    
with open("Day_10\\input.txt", "r") as input:
    for line in input:
        maze.append(line.strip())

# Now we need to find the start location.
start_location = []
for line_index in range(len(maze)):
    if "S" in maze[line_index]:
        start_location = [line_index, maze[line_index].index("S")]
        break

# Now we have the start location we run two routes through each connecting pipe until they are on the same coordinate, which is our final answer.
global coordinates_checked
coordinates_checked = [[start_location], [start_location]]
next_to_check = find_first_two_pipes(start_location)

step_count = 1
while True:
    step_count += 1
    for side in range(2):
        coordinates_checked[side].append(next_to_check[side])
        next_to_check[side] = find_next_position_to_check(next_to_check[side], side)
    
    if next_to_check[0] == next_to_check[1]:
        break

print(step_count)
