total = 0

with open("Day_2\\input.txt", "r") as input:
    for line in input:
        game_number = int(line.strip().split(":")[0].split(" ")[1])
        game_rounds = line.strip().split(":")[1].split(";")
        min_red = 0
        min_green = 0
        min_blue = 0
        for round in game_rounds:
            set = round.strip().split(",")
            for cube_colour in set:
                number = int(cube_colour.strip().split(" ")[0])
                colour = cube_colour.strip().split(" ")[1]
                if "red" in colour.lower():
                    if number > min_red:
                        min_red = number
                elif "green" in colour.lower():
                    if number > min_green:
                        min_green = number
                elif "blue" in colour.lower():
                    if number > min_blue:
                        min_blue = number
        
        total += min_red * min_green * min_blue
                
print(total)
