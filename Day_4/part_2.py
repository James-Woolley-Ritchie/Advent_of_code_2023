# Make a dictionary with all of the cards in.
cards = {}

# Keep track of every card that needs checking. (So we can include copies)
card_numbers_to_check = []

# Add every card to the dictionary of cards.
with open("Day_4\\input.txt", "r") as input:
    for line in input:
        card = line.strip().replace("  ", " ").split("|") # Get rid of any double spaces, the are very annoying.
        card_number = card[0].split(":")[0].split(" ")[-1].strip()
        winning_numbers = card[0].split(":")[1].strip().split(" ")
        card_numbers = card[1].strip().split()
        cards.update({card_number : [card_numbers, winning_numbers]})

# Now we have all of the cards, add all of the card numbers to the list to check.
for number in range(len(cards)):
    card_numbers_to_check.append(number + 1)

# We now have the numbers we need to check, so we can iterate through them.
for card_number in card_numbers_to_check:
    card = cards.get(str(card_number))
    number_of_copies = 0
    for number in card[0]:
        for winning_number in card[1]:
            if number == winning_number:
                number_of_copies += 1
    for i in range(number_of_copies): 
        card_numbers_to_check.append(card_number + i + 1)

print(len(card_numbers_to_check))