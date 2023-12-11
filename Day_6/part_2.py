with open("Day_6\\input.txt", "r") as input:
    time = int(input.readline().replace(" ", "").split(":")[1].strip())
    distance = int(input.readline().replace(" ", "").split(":")[1].strip())

    number_of_possible_wins = 0

    # distance = speed * time
    # Find the first one.
    milliseconds_minimim = 0
    for time_held in range(time):
        time_travelling = time - time_held
        possible_distance = time_held * time_travelling
        if possible_distance > distance:
            milliseconds_minimim = time_held
            break

    milliseconds_maximum = 0
    for time_travelling in range(time):
        time_held = time - time_travelling
        possible_distance = time_travelling * time_held
        if possible_distance > distance:
            milliseconds_maximum = time_held
            break

    number_of_possible_wins = milliseconds_maximum - milliseconds_minimim + 1 # + 1 because inclusive.

print(number_of_possible_wins)