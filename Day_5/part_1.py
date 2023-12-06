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
        if int(key) in range(int(map[i][1]), int(map[i][1]) + int(map[i][2]) - 1): # If it's in the defined range.
            return int(map[i][0]) + int(key) - int(map[i][1])
        
    return None

# Iterate through the input.
with open("Day_5\\input.txt", "r") as input:
    # Get the lists of seeds.
    seeds = input.readline().replace("\n", "").split(":")[1].strip().split(" ")
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

for seed in seeds:
    soil = Find_in_map(seed_to_soil, seed)
    if soil == None: 
        soil = seed
    
    fertilizer = Find_in_map(soil_to_fertilizer, soil)
    if fertilizer == None:
        fertilizer = soil

    water = Find_in_map(fertilizer_to_water, fertilizer)
    if water == None:
        water = fertilizer

    light = Find_in_map(water_to_light, water)
    if light == None:
        light = water

    temperature = Find_in_map(light_to_temperature, light)
    if temperature == None:
        temperature = light

    humidity = Find_in_map(temperature_to_humidity, temperature)
    if humidity == None:
        humidity = temperature

    location = Find_in_map(humidity_to_location, humidity)
    if location == None:
        location = humidity

    if lowest_location_number == None: # Not been set yet.
        lowest_location_number = location
    elif location < lowest_location_number:
        lowest_location_number = location

print(lowest_location_number)