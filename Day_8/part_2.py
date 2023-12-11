import math

sequence = ""
nodes = {}
starting_nodes = []
ending_nodes = []

with open ("Day_8\\input.txt", "r") as input:
    sequence = input.readline().strip()
    input.readline()

    for line in input:
        nodes.update({line.split("=")[0].strip() : (line.split("=")[1].replace("(", "").replace(")", "").split(",")[0].strip(), line.split("=")[1].replace("(", "").replace(")", "").split(",")[1].strip())})
        if line.split("=")[0].strip()[-1] == 'A':
            starting_nodes.append(line.split("=")[0].strip()) # Find all of the nodes that we need to start on.
        
# Now we need to find the number of steps for each start point to get to an end point.
number_of_steps_to_reach_end = []

for starting_node_index in range(len(starting_nodes)):
    number_of_steps_to_reach_end.append(0)
    step_count = 0
    found = False

    node = starting_nodes[starting_node_index]

    while not found:
        for step in sequence:
            step_count += 1 # Increment step count

            if step == 'L':
                node = nodes.get(node)[0]

            else:
                node = nodes.get(node)[1]

            if node[-1] == 'Z':
                found = True
                ending_nodes.append(node)
                number_of_steps_to_reach_end[starting_node_index] = step_count
                break

print(starting_nodes)
print(number_of_steps_to_reach_end)
print(ending_nodes)

number_of_steps_to_reach_self = []

for ending_node_index in range(len(ending_nodes)):
    number_of_steps_to_reach_self.append(0)
    step_count = 0
    
    sequence_step = (number_of_steps_to_reach_end[ending_node_index] - 1) % len(sequence)

    node = ending_nodes[ending_node_index]

    while True:
        step_count += 1 # Increment step count
        step = sequence[sequence_step]

        if step == 'L':
            node = nodes.get(node)[0]

        else:
            node = nodes.get(node)[1]

        if node == ending_nodes[ending_node_index]:
            number_of_steps_to_reach_self[ending_node_index] = step_count
            break

# Now we know how many iterations to get to the end node initally for each starting node, and how many iterations additionally to reach the end node again after that.
# Do some motherfucking maths.
# 17141 + 61a = x
# 16579 + 59b = x
# 18827 + 67c = x
# 12083 + 43d = x
# 13027 + 47e = x
# 22199 + 79f = x

print(math.lcm(*[number_of_steps_to_reach_end[index] for index in range(len(starting_nodes))]))