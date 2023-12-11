total = 0

possible_cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

hands = [
    "five of a kind",
    "four of a kind",
    "full house",
    "three of a kind",
    "two pair",
    "one pair",
    "high card"
]

game_hands = []

def find_hand_type(hand):
    number_of_each_card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in hand:
        number_of_each_card[possible_cards.index(card)] += 1

    for number in number_of_each_card:
        if number == 5:
            return "five of a kind"
        elif number == 4:
            return "four of a kind"
        elif number == 3:
            if 2 in number_of_each_card:
                return "full house"
            else:
                return "three of a kind"
        elif number == 2:
            if 3 in number_of_each_card: # In case the two cards are two higher cards than the 3
                return "full house"
            elif number_of_each_card.count(2) == 2:
                return "two pair"
            else:
                return "one pair"
    return "high card"

def find_if_stronger(current_hand, checking_hand):
    if hands.index(find_hand_type(current_hand)) < hands.index(find_hand_type(checking_hand)):
        return True
    elif hands.index(find_hand_type(current_hand)) > hands.index(find_hand_type(checking_hand)):
        return False
    else:
        for card_index in range(len(current_hand)):
            if possible_cards.index(current_hand[card_index]) < possible_cards.index(checking_hand[card_index]):
                return True
            elif possible_cards.index(current_hand[card_index]) > possible_cards.index(checking_hand[card_index]):
                return False

# iterate through the lines in the file.
with open("Day_6\\input.txt", "r") as input:
    for line in input:
        current_hand = line.strip().split(" ")[0]
        inserted = False
        for hand_index in range(len(game_hands)):
            if not find_if_stronger(current_hand, game_hands[hand_index]): # Sort from weakest to strongest
                game_hands.insert(hand_index, current_hand)
                inserted = True
                break
        if not inserted:
            game_hands.append(current_hand)            

with open("Day_6\\input.txt", "r") as input: 
    for line in input:
        total += (game_hands.index(line.strip().split()[0]) + 1) * int(line.strip().split()[1])

print(total)