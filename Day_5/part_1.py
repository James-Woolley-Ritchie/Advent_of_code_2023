with open("Day_5\\input.txt", "r") as file:
    data = file.read()
    sources, *data_blocks = data.split("\n\n")

sources = list(map(int, sources.split(":")[1].split()))

for data_block in data_blocks:
    ranges_list = []
    for line in data_block.splitlines()[1:]:
        ranges_list.append(list(map(int, line.split())))

    destinations = []

    for current_source in sources:
        for destination, source, length in ranges_list:
            if current_source in range(source, source + length + 1):
                destinations.append(current_source - source + destination)
                break
        else:
            destinations.append(current_source)

    sources = destinations

smallest_location = min(destinations)
print(smallest_location)