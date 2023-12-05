total = 0

with open("Day_4\\input.txt", "r") as input:
    for line in input:
        card = line.strip().split("|")
        winning_numbers = card[0].split(":")[1].strip().split(" ")
        card_numbers = card[1].strip().split()
        points = 0
        for card_number in card_numbers:
            for winning_number in winning_numbers:
                if card_number == winning_number: # Point(s), but how many?
                    if points >= 1:
                        points *= 2
                    else:
                        points = 1
        total += points

print(total)