total = 0

with open("Day_9\\input.txt", "r") as input:
    for line in input:
        numbers = []
        for number in line.strip().split(" "):
            numbers.append(int(number))

        differences = []
        differences.append(numbers)
        all_zero = False
        count = 0
        while not all_zero:
            all_zero = True
            previous_differences = differences[count]
            count += 1
            current_differences = []

            for index in range(len(numbers) - count):
                current_differences.append(previous_differences[index + 1] - previous_differences[index])
                if previous_differences[index + 1] - previous_differences[index] != 0:
                    all_zero = False

            differences.append(current_differences)

        # Now we have the differences up to the point they are all 0.
        # Add the new value to the end of the row.
        differences[-1].append(0) # Add a zero to the end of the last row of differences

        for differences_index in range(len(differences) - 1):
            differences[-1 * (differences_index + 2)].insert(0, differences[-1 * (differences_index + 2)][0] - differences[-1 * (differences_index + 1)][0])

        total += differences[0][0]

print(total)