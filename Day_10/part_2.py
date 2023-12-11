# 5 minutes in to part 2 and I already want to kill myself.
# Challenge accepted AoC admins... Let's start the timer gadies and lentlemen! Starting @ 23:44

# What if we find every loop of pipe, then find the number of dots enclosed in this pipe.
# Keep track of the coordinates in each loop - run left to right on each line between the leftmost and second leftmost etc counting the "."s

# Here we have the code from part 1... let's revamp this shit.
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# First we will need access to the full file in array form. -- Still true
global maze 
maze = []

# Defining functions.
def find_first_two_pipes(coordinates): # To check which two pipes are valid from the start point. -- Need to add a return None if there are not two connecting pipes.
    pipes = []

    # We need to make sure this fucker doesn't start going backwards.
    if coordinates[0] > 1:
        if maze[coordinates[0] - 1][coordinates[1]] in ["|", "7", "F"]: # Checks if connected to above pipe.
            # We don't KNOW this is a loop so we need to double check this fucker.
            if maze[coordinates[0]][coordinates[1]] in ["|", "J", "L"]:
                pipes.append([coordinates[0] - 1, coordinates[1]])
                if len(pipes) == 2:
                    return pipes
            
    if coordinates[1] > 1:
        if maze[coordinates[0]][coordinates[1] - 1] in ["-", "L", "F"]: # Checks if connected to left pipe.
            if maze[coordinates[0]][coordinates[1]] in ["-", "J", "7"]:
                pipes.append([coordinates[0], coordinates[1] - 1])
                if len(pipes) == 2:
                    return pipes
    
    # Make sure this fucker isn't going off the map.
    if coordinates[1] < len(maze[coordinates[0]]) - 1:
        if maze[coordinates[0]][coordinates[1] + 1] in ["-", "J", "7"]: # Checks if connected to right pipe.
            if maze[coordinates[0]][coordinates[1]] in ["-", "L", "F"]:
                pipes.append([coordinates[0], coordinates[1] + 1])
                if len(pipes) == 2:
                    return pipes
    
    if coordinates[0] < len(maze) - 1:
        if maze[coordinates[0] + 1][coordinates[1]] in ["|", "J", "L"]: # Checks if connected to below pipe.
            if maze[coordinates[0]][coordinates[1]] in ["|", "F", "7"]:
                pipes.append([coordinates[0] + 1, coordinates[1]])
                if len(pipes) == 2:
                    return pipes
        
    return None # Will only ever reach this point if there are not two adjoining pipes.

def find_next_position_to_check(coordinates, side): # -- This can stay the same as far as I'm concerned.
    pipe = maze[coordinates[0]][coordinates[1]]
    output = [-1, -1]

    match pipe:
        case "|":
            if [coordinates[0] - 1, coordinates[1]] in coordinates_checked[side]: # Just come from the top.
                # Again, bellend over here forgot that we don't know for definite that this is a loop so we have to double check EVERY FUCKING STEP
                try:
                    if maze[coordinates[0] + 1][coordinates[1]] in ["|", "J", "L"]:
                        output = [coordinates[0] + 1, coordinates[1]] # down
                except: pass
            
            else:
                try:
                    if maze[coordinates[0] - 1][coordinates[1]] in ["|", "F", "7"]:
                        output = [coordinates[0] - 1, coordinates[1]] # up
                except: pass
            
        case "-":
            if [coordinates[0], coordinates[1] - 1] in coordinates_checked[side]: # Just come from the left.
                try:
                    if maze[coordinates[0]][coordinates[1] + 1] in ["-", "J", "7"]:
                        output = [coordinates[0], coordinates[1] + 1] # right
                except: pass
            
            else:
                try:
                    if maze[coordinates[0]][coordinates[1] - 1] in ["-", "F", "L"]:
                        output = [coordinates[0], coordinates[1] - 1] # left
                except: pass
        
        case "L":
            if [coordinates[0] - 1, coordinates[1]] in coordinates_checked[side]: # Just come from the top.
                try:
                    if maze[coordinates[0]][coordinates[1] + 1] in ["-", "J", "7"]:
                        output = [coordinates[0], coordinates[1] + 1] # right
                except: pass
            
            else:
                try:
                    if maze[coordinates[0] - 1][coordinates[1]] in ["|", "F", "7"]:
                        output = [coordinates[0] - 1, coordinates[1]] # up
                except: pass
                
        case "J":
            if [coordinates[0] - 1, coordinates[1]] in coordinates_checked[side]: # Just come from the top.
                try:
                    if maze[coordinates[0]][coordinates[1] - 1] in ["-", "F", "L"]:
                        output = [coordinates[0], coordinates[1] - 1] # left
                except: pass
            
            else:
                try:
                    if maze[coordinates[0] - 1][coordinates[1]] in ["|", "F", "7"]:
                        output = [coordinates[0] - 1, coordinates[1]] # up
                except: pass
            
        case "7":
            if [coordinates[0], coordinates[1] - 1] in coordinates_checked[side]: # Just come from the left.
                try:
                    if maze[coordinates[0] + 1][coordinates[1]] in ["|", "J", "L"]:
                        output = [coordinates[0] + 1, coordinates[1]] # down
                except: pass
            
            else:
                try:
                    if maze[coordinates[0]][coordinates[1] - 1] in ["-", "F", "L"]:
                        output = [coordinates[0], coordinates[1] - 1] # left
                except: pass
            
        case "F":
            if [coordinates[0], coordinates[1] + 1] in coordinates_checked[side]: # Just come from the right.
                try:
                    if maze[coordinates[0] + 1][coordinates[1]] in ["|", "J", "L"]:
                        output = [coordinates[0] + 1, coordinates[1]] # down
                except: pass
            
            else:
                try:
                    if maze[coordinates[0]][coordinates[1] + 1] in ["-", "J", "7"]:
                        output = [coordinates[0], coordinates[1] + 1] # right
                except: pass
            
    if output[0] < 0 or output[1] < 0:
        return None
    
    return output # YOU DIDN'T RETURN THE OUTPUT YOU SHIT FOR BRAINS FUCKING IMBECILE
    
def find_every_pipe_in_loop(starting_position):
    coordinates_checked.clear()
    coordinates_checked.append([starting_position])
    coordinates_checked.append([starting_position])
    loop = [starting_position]
    # Now we have the start location we run two routes through each connecting pipe until they are on the same coordinate, which is our final answer.
    next_to_check = find_first_two_pipes(starting_position)

    step_count = 1
    while True:
        step_count += 1
        for side in range(2):
            coordinates_checked[side].append(next_to_check[side])
            loop.append(next_to_check[side])
            next_to_check[side] = find_next_position_to_check(next_to_check[side], side)

        if next_to_check[0] == None or next_to_check[1] == None:
            break # Gone off the map hence not enclosed.
        
        if next_to_check[0] == next_to_check[1]:
            loop.append(next_to_check[0])
            if [22, 91] in loop: # Only the main loop
                loops.append(loop) # Now we know it's a complete loop we add it to the list.
            coordinates_checked[0].pop(0) # Remove one of the starting positions' so there are no dupes.
            total_coordinates_checked.append(next_to_check[0])
            for coordinate_checked in coordinates_checked[0]:
                total_coordinates_checked.append(coordinate_checked)
            for coordinate_checked in coordinates_checked[1]:
                total_coordinates_checked.append(coordinate_checked) # There's no point ever checking these fuckers again because loops don't cross over ofc
            break

with open("Day_10\\input_part_2.txt", "r") as input:
    for line in input:
        maze.append(line.strip())

# Now we need to find the start location. -- Time for the big fuck off changes, let's go girls!
# But first we need to keep track of the total, remember it's only one number!
total = 0 # This fucking integer is going to be the bane of my existence for the night!

global coordinates_checked
coordinates_checked = [[], []]

global total_coordinates_checked
total_coordinates_checked = []

global loops
loops = []

# For the puposes of part 2, a start position is the next position we find that we haven't already checked.
# Now I had to cheat here and change the S for what I know it is because cannot be fucked doing that programatically for no fucking reason!
# S is J in this case FYI xoxoxo
for row in range(len(maze)):
    for column in range(len(maze[0])):
        if [row, column] not in total_coordinates_checked and find_first_two_pipes([row, column]) != None: # Now to find every pipe in the loop.
            find_every_pipe_in_loop([row, column]) # Let's give this fucker a good go!

# find_every_pipe_in_loop(0, [22, 91]) # Debugging purposes, [22, 91] is the starting index.
# # Of course it's still finding no fucking loops.
# # What the actual fuck.

# If this fucking works first time I swear to god I'm a fucking genius. -- I'm not...

# Why won't this peice of shit just give me a fucking answer already.

# Why the fuck is it finding no loops, my brother in christ you've already found a loop in this maze!!!! WHY ARE YOU BEING SO TEMPERAMENTAL YOU PEICE OF SHIT!?!?!?!?!?!?

# I've had enough of this shit, can't be fucked with it anymore.
# Now we need to identify which of the tiles that aren't in a loop are fully enclosed and which are not
# Just more fucking endless joys.
# Look at which letters block which directions then follow the "0s" start with two big fuck off lists of those in loops and those not.

# So we can see what the fuck we are doing, make a new text file with all the loops the same but everything else as a "." so we can see what we are looking at here.
# Worst comes worst I'll fucking count them myself.
with open("Day_10\\better_input.txt", "w") as better_input:
    for row_index in range(len(maze)):
        for column_index in range(len(maze[0])):
            found = False
            for loop in loops:
                if [row_index, column_index] in loop:
                    better_input.write(maze[row_index][column_index])
                    found = True
                    break
            if not found:
                better_input.write(".")
        better_input.write("\n")

better_maze = []
with open("Day_10\\better_input.txt", "r") as input:
    for line in input:
        better_maze.append(line.strip())

# Now we have this big fuck off maze we count how many dots there are first, then go from every outermost point and find every adjacent dot (no duplicates) and remove that count from the total.
dot_count = 0

for row in better_maze:
    for pipe in row:
        if pipe == ".":
            dot_count += 1

# Now to write a recursive function to find the positions of all adjoining dots.
global non_enclosed_dots 
non_enclosed_dots = []

# Populate with all dots that are on the outer layer.
for pipe_index in range(len(better_maze[0])):
    if better_maze[0][pipe_index] == ".":
        non_enclosed_dots.append([0, pipe_index])

for pipe_index in range(len(better_maze[-1])):
    if better_maze[-1][pipe_index] == ".":
        non_enclosed_dots.append([len(better_maze) - 1, pipe_index])

for row_index in range(1, len(better_maze) - 1):
    if better_maze[row_index][0] == ".":
        non_enclosed_dots.append([row_index, 0])
    if better_maze[row_index][-1] == ".":
        non_enclosed_dots.append([row_index, len(better_maze[row_index]) - 1])

def find_surrounding_dots(dot_coordinate):
    coordinates_to_check = [[dot_coordinate[0] - 1, dot_coordinate[1] - 1], 
                            [dot_coordinate[0] - 1, dot_coordinate[1]], 
                            [dot_coordinate[0] - 1, dot_coordinate[1] + 1], 
                            [dot_coordinate[0], dot_coordinate[1] - 1], 
                            [dot_coordinate[0], dot_coordinate[1] + 1], 
                            [dot_coordinate[0] + 1, dot_coordinate[1] - 1], 
                            [dot_coordinate[0] + 1, dot_coordinate[1]], 
                            [dot_coordinate[0] + 1, dot_coordinate[1] + 1]]

    for coordinate in coordinates_to_check:
        if coordinate[0] >= 0 and coordinate[0] < len(better_maze) and coordinate[1] >= 0 and coordinate[1] < len(better_maze[0]): # Make sure it's within the right ranges.
            if better_maze[coordinate[0]][coordinate[1]] == "." and [coordinate[0], coordinate[1]] not in non_enclosed_dots:
                non_enclosed_dots.append([coordinate[0], coordinate[1]])

# Now use the function.
for dot in non_enclosed_dots:
    find_surrounding_dots(dot)

# Then print out the total.
total = dot_count - len(non_enclosed_dots)


# It's still saying it's wrong, let's see why.
with open("Day_10\\yet_another_input.txt", "w") as output:
    for row_index in range(len(better_maze)):
        for column_index in range(len(better_maze[0])):
            if [row_index, column_index] in non_enclosed_dots:
                output.write("#")
            else:
                output.write(better_maze[row_index][column_index])
        output.write("\n")

# Now I still need to find the routes they could slip down. How on earth am I meant to do that.
# No I don't.
final_maze = []
enclosed = []

with open("Day_10\\yet_another_input.txt", "r") as input:
    for line in input:
        final_maze.append(line.strip())

def find_if_inside(point):
    count = 0
    for pipe_column in range(point[1], -1, -1):
        if final_maze[point[0]][pipe_column] in ["J", "L", "|"]:
            count += 1
    if count % 2 == 1: # Odd number means inside.
        return True

# Let's finish off this motherfucker.
for row in range(len(final_maze)):
    for column in range(len(final_maze[row])):
        if final_maze[row][column] == ".":
            # Now count left.
            if find_if_inside([row, column]):
                if [row, column] not in enclosed:
                    enclosed.append([row, column])
            
print(enclosed)
print(len(enclosed))



