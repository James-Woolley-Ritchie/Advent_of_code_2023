lowest_location_number = None

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

def Find_in_map(map, key):
    for i in range(len(map)):
        if int(key) in range(int(map[i][1]), int(map[i][1]) + int(map[i][2]) + 1): # If it's in the defined range.
            return int(map[i][0]) + int(key) - int(map[i][1])
        
    return None

def Find_from_value_in_map(map, value):
    for i in range(len(map)):
        if int(value) in range(int(map[i][0]), int(map[i][0]) + int(map[i][2])):
            return int(map[i][1]) + int(value) - int(map[i][0])
        
    return None

# Iterate through the input.
with open("Day_5\\input.txt", "r") as input:
    # Get the lists of seeds.
    top_line = input.readline().replace("\n", "").split(":")[1].strip().split(" ")
    i = 0
    while i in range(len(top_line)):
        seeds.append([top_line[i], top_line[i+1]])
        i += 2
    input.readline() # Skip the empty line.

    # Go through the lines containing the maps.
    current_map = ""
    for line in input:
        if "map" in line.lower():
            current_map = line.split(" ")[0]
        
        else:
            if line.strip() != "":
                if current_map == "seed-to-soil":
                    seed_to_soil.append(line.strip().split(" "))
                elif current_map == "soil-to-fertilizer":
                    soil_to_fertilizer.append(line.strip().split(" "))
                elif current_map == "fertilizer-to-water":
                    fertilizer_to_water.append(line.strip().split(" "))
                elif current_map == "water-to-light":
                    water_to_light.append(line.strip().split(" "))
                elif current_map == "light-to-temperature":
                    light_to_temperature.append(line.strip().split(" "))
                elif current_map == "temperature-to-humidity":
                    temperature_to_humidity.append(line.strip().split(" "))
                elif current_map == "humidity-to-location":
                    humidity_to_location.append(line.strip().split(" "))
found = False
lowest_location_number = 37383999

while not found:
    humidity = Find_from_value_in_map(humidity_to_location, lowest_location_number)
    if humidity == None:
        humidity = lowest_location_number
    
    temperature = Find_from_value_in_map(temperature_to_humidity, humidity)
    if temperature == None:
        temperature = humidity

    light = Find_from_value_in_map(light_to_temperature, temperature)
    if light == None:
        light = temperature

    water = Find_from_value_in_map(water_to_light, light)
    if water == None:
        water = light

    fertilizer = Find_from_value_in_map(fertilizer_to_water, water)
    if fertilizer == None:
        fertilizer = water

    soil = Find_from_value_in_map(soil_to_fertilizer, fertilizer)
    if soil == None:
        soil = fertilizer

    seed = Find_from_value_in_map(seed_to_soil, soil)
    if seed == None:
        seed = soil

    for possible_seed in seeds:
        if int(seed) in range(int(possible_seed[0]), int(possible_seed[0]) + int(possible_seed[1]) - 1):
            found = True
            break

    if not found:
        lowest_location_number += 1

    if lowest_location_number > 37385000:
        break

print(lowest_location_number)

