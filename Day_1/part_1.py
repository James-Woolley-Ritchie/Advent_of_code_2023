total = 0
with open("input.txt", "r") as input:
    for line in input:
        first_number = None
        second_number = None
        for character in line:
            try:
                if first_number == None:
                    first_number = int(character)
                second_number = int(character)
            except:
                pass
        total += (int(str(first_number) + str(second_number)))
print(total)

