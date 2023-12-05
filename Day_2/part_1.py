total = 0

with open("Day_2\\input.txt", "r") as input:
    for line in input:
        game_number = int(line.strip().split(":")[0].split(" ")[1])
        game_rounds = line.strip().split(":")[1].split(";")
        possible = True
        for round in game_rounds:
            set = round.strip().split(",")
            for cube_colour in set:
                number = int(cube_colour.strip().split(" ")[0])
                colour = cube_colour.strip().split(" ")[1]
                if "red" in colour.lower() and number > 12:
                    possible = False
                elif "green" in colour.lower() and number > 13:
                    possible = False
                elif "blue" in colour.lower() and number > 14:
                    possible = False
        if possible:
            total += game_number
                
print(total)
