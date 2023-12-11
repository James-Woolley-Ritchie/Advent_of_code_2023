total = 1

with open("Day_6\\input.txt", "r") as input:
    times = input.readline().replace("  ", "").split(":")[1].strip().split(" ")
    distances = input.readline().replace("  ", "").split(":")[1].strip().split(" ")

    for match in range(len(times)):
        number_of_possible_wins = 0

        # distance = speed * time
        for time_held in range(int(times[match])):
            time_travelling = int(times[match]) - time_held
            distance = time_held * time_travelling
            if distance > int(distances[match]):
                number_of_possible_wins += 1

        total *= number_of_possible_wins

print(total)