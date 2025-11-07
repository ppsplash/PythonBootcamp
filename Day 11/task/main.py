import random
from art import logo

c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_card = []
comp_card = []
total = 0


def user_card():
    my_card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Your cards: {my_card}, current score: {sum(my_card)}")
    return my_card


def computer_card():
    comp_card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 1)
    print(f"Computer's first card: {comp_card}")
    return comp_card


def adding_cards(my_card, comp_card):
    my_card.append(random.choice(c))
    print(f"Your cards: {my_card}, current score: {sum(my_card)}")
    print(f"Computer's first card: {comp_card}")
    if sum(my_card) > 21 and 11 not in my_card:
        print("You went over. You lose :(")
        exit()
    return total


def adding_computer_cards(my_card, comp_card):
    while sum(comp_card) < 17:
        comp_card.append(random.choice(c))
    print(f"Your final hand: {my_card} , final score : {sum(my_card)}")
    print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")
    if sum(comp_card) > 21:
        print("Opponent went over. You win:)")
    elif sum(comp_card) <= 21 and sum(comp_card) > sum(my_card):
        print("Opponent win!!!!. You lose")
    elif sum(comp_card) <= 21 and sum(comp_card) == sum(my_card):
        print("Draw")
    elif sum(comp_card) <= 21 and sum(my_card) > sum(comp_card):
        print("You win!!")
    elif sum(my_card) > 21 and 11 in my_card:
        my_card.remove(11)
        my_card.append(1)
        print(f"Your cards: {my_card}, current score: {sum(my_card)}")
        print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")


def validation(total):
    if total == 21 and 11 in my_card:
        print(f"Your final hand: {my_card} , final score : {total}")
        print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")
        print("Win with a Blackjack:)")
        exit()
    if total == 21 and 11 in comp_card:
        print(f"Your final hand: {my_card} , final score : {total}")
        print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")
        print("Lose with a Blackjack:)")
        exit()
    if total > 21 and 11 in my_card:
        my_card.remove(11)
        my_card.append(1)
        total = sum(my_card)
        print(f"Your cards: {my_card}, current score: {total}")
        print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")


def start():
    print(logo)
    my_card = user_card()
    comp_card = computer_card()
    total = sum(my_card)
    validation(total)
    repeat = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
    while repeat == 'y':
        adding_cards(my_card, comp_card)
        total = sum(my_card)
        validation(total)
        repeat = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
    while repeat == 'n':
        adding_computer_cards(my_card, comp_card)
        total = sum(my_card)
        validation(total)
        exit()


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower() == 'y':
    print("\n" * 30)
    start()
