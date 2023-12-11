step_count = 0
sequence = ""
nodes = {}

with open ("Day_8\\input.txt", "r") as input:
    sequence = input.readline().strip()
    input.readline()

    for line in input:
        nodes.update({line.split("=")[0].strip() : (line.split("=")[1].replace("(", "").replace(")", "").split(",")[0].strip(), line.split("=")[1].replace("(", "").replace(")", "").split(",")[1].strip())})
        
# Now we have the sequence and the nodes dictionary, we can run the sequence.
current_node = "AAA"
finished = False

while not finished: # Repeat the sequence until we are finished.
    for step in sequence:
        step_count += 1 # Increment step count

        if step == 'L':
            current_node = nodes.get(current_node)[0]

        else:
            current_node = nodes.get(current_node)[1]

        if current_node == "ZZZ":
            finished = True
            break

print(step_count)