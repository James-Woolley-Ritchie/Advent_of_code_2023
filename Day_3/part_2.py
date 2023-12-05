# We want to read everything into a local 2d array first.
schematic = []
total = 0

special_character_indexes = []
numbers_and_indexes = []

with open("Day_3\\input.txt", "r") as input:
    for line in input:
        schematic.append(line.strip())
    
    for line_index in range(len(schematic)):
        for character_index in range(len(schematic[line_index])):
            if schematic[line_index][character_index] == "*":
                special_character_indexes.append([line_index, character_index]) # Find the indexes of all the *.

    # Now we need to go through each line and if we find a digit, keep going until we have found the index of all up to three characters.
    for line_index in range(len(schematic)):
        previous_is_digit = False
        for character_index in range(len(schematic[line_index])):
            if schematic[line_index][character_index].isdigit() and not previous_is_digit: # Start of a new number
                number = [schematic[line_index][character_index], [line_index, character_index], ["-", "-"], ["-", "-"]]
                previous_is_digit = True
                if character_index + 1 == len(schematic[line_index]): # End of the line hence end of number.
                    numbers_and_indexes.append(number)
                    previous_is_digit = False
            elif schematic[line_index][character_index].isdigit() and previous_is_digit: # Continuation of number
                if number[2] == ["-", "-"]:
                    number[0] = number[0] + schematic[line_index][character_index]
                    number[2] = [line_index, character_index]
                else:
                    number[0] = number[0] + schematic[line_index][character_index]
                    number[3] = [line_index, character_index]
                if character_index + 1 == len(schematic[line_index]): # End of the line hence end of number.
                    numbers_and_indexes.append(number)
                    previous_is_digit = False
            elif not schematic[line_index][character_index].isdigit() and previous_is_digit: # End of number
                numbers_and_indexes.append(number)
                previous_is_digit = False

    # Now we have all the information we need to know if we need to add the number to the total.
    for special_character_index in special_character_indexes:
        indexes_to_check = []
        for i in range(3):
            for j in range(3):
                indexes_to_check.append([special_character_index[0] - 1 + i, special_character_index[1] - 1 + j])
        number_of_adjacent = 0
        adjacent_numbers = []
        for number_and_indexes in numbers_and_indexes:
            valid_number = False
            for i in range(3):
                for index in indexes_to_check:
                    if number_and_indexes[i + 1] == index:
                        number_of_adjacent += 1
                        adjacent_numbers.append(number_and_indexes[0])
                        valid_number = True
                        break
                if valid_number:
                    break
        
        # Now check if there were exactly two.
        if number_of_adjacent == 2:
            product = int(adjacent_numbers[0]) * int(adjacent_numbers[1])
            total += product

print(total)
