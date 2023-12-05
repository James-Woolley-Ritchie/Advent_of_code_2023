# Set total to 0.
total = 0

# List of numbers.
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Open the file.
with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        print("-------------------")

        # Set the numbers initially to blank so we know once we have found the first occurence.
        first_number = None
        second_number = None
        print("Old: " + line)

        if ("tmlsix2fiveninefourgjltplkfcnine" in line):
            print("test")

        # Set the inital values of too high and too low so we can compare against them later.
        first_number_index = 100000
        last_number_index = -1
        first_spelled_number = ""
        last_spelled_number = ""

        # Iterate through the numbers in the list ("one" to "nine")
        for index in range(len(numbers)):
            current_number_index = line.find(numbers[index]) # Find the first occurence of this number
            if current_number_index != -1: # If there is an occurence of this in the line

                # Find out if this appears earlier than the "current" first number index
                if current_number_index < first_number_index:
                    first_number_index = current_number_index # Update first number index
                    first_spelled_number = numbers[index] # Keep track of which number it was.

                # Find out if this appears later than the "current" last number index
                while (line.find(numbers[index], current_number_index + 1) != -1): # Update last number index that we are checking to make sure we are checking against the last occurence of this spelled number.
                    current_number_index = line.find(numbers[index], current_number_index + 1) # Find the next occurence
                if current_number_index > last_number_index:
                    last_number_index = current_number_index # Update last number index
                    while (line.find(numbers[index], last_number_index + 1) != -1): # Keep finding the next occurence of this number so we keep track of the index of it's last occurence or it may be overriden by a number between two occurences.
                        last_number_index = line.find(numbers[index], last_number_index + 1) # Find the next occurence
                    last_spelled_number = numbers[index] # Keep track of the actual number
        
        # If a digit occurs before the first written number we need to make sure we don't mess with the "first" occurence e.g 5oneight should be 5on8 -> 58 rather than 51ight -> 51.
        for character in line:
            if character.isdigit() and line.index(character) < first_number_index:
                first_spelled_number = "" # Now it will be ignored.

        # Replace ONLY the first occurence of the first written number if it exists e.g. one67xoneight should turn to 167xon8 rather than 167x1ight
        if (first_spelled_number != ""):
            line = line.replace(first_spelled_number, str(numbers.index(first_spelled_number) + 1), 1)
        
        # Replace ALL occurences of the last written number if it exists because it now no longer matters!
        if (last_spelled_number != ""):
            line = line.replace(last_spelled_number, str(numbers.index(last_spelled_number) + 1))

        print("New: " + line)
        # Find the first and last digit, combine them, and add to the total.
        for character in line:
            try:
                if first_number == None:
                    first_number = int(character)
                second_number = int(character)
            except:
                pass
        print("Digits: " + str(first_number) + str(second_number))
        total += (int(str(first_number) + str(second_number)))
        print("Current total: " + str(total))

print(total)