import random
from art import logo

c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def user_card():
    global card
    my_card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Your cards: {card}, current score: {sum(card)}")
    if sum(my_card) > 21 and 11 in card:
        card.remove['11']
        card.append['1']
        print(f"Your final hand: {card}, final score: {sum(card)}")
    elif sum(my_card) > 21:
        print(f"Your final hand: {card}, final score: {sum(card)}")
        print(f"Computer#s final hand: {compcard}, final score. {compcard}")
        print("You went over. You lose")


def adding_cards():
    next = input("Type 'y' to get an another card, type 'n' to pass: ").lower()
    if next == 'y':
        card.append(random.choice(c))
        print(f"Your cards: {card}, current score: {sum(card)}")
    else:
        while next == 'n' and sum(compcard) < 17:
            compcard.append(random.choice(c))
    print(f"Your final hand: {card}, final score: {sum(card)}")
    print(f"Computer's final hand: {compcard}, final score. {compcard}")
    print("Opponent went over. You win :)")


def not_adding_cards():
    print(f"Your final hand: {card}, final score: {sum(card)}")
    print(f"Computer#s final hand: {compcard}, final score. {compcard}")
    print("You went over. You lose")


def computer_card():
    global compcard
    compcard = random.choice(c)
    print(f"Computer's first card: {compcard}")


def adding_comp_card():
    if sum(compcard) < 17:
        compcard.append(random.choice(c))
        print(f"Computer's final hand: {compcard}, final score: {sum(compcard)}")
        print("Opponent went over. You win :)")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if start == 'y':
    print(logo)
    user_card()
    computer_card()
    while sum(card) < 21:
        adding_cards()
    if sum(card) > 21:
        not_adding_cards()
    if sum(card) == 21:
        adding_comp_card()
