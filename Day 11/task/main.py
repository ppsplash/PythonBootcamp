import random
from art import logo

c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def user_card():
    global card
    card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Your cards: {card}, current score: {sum(card)}")
    if sum(card) > 21:
        print(f"Your final hand: {card}, final score: {sum(card)}")
        print(f"Computer#s final hand: {comp_card}, final score. {comp_card}")
        print("You went over. You lose")


def adding_cards():
    next = input("Type 'y' to get an another card, type 'n' to pass: ").lower()
    if next == 'y':
        card.append(random.choice(c))
        print(f"Your cards: {card}, current score: {sum(card)}")
    else:
        exit()


def not_adding_cards():
    print(f"Your final hand: {card}, final score: {sum(card)}")
    print(f"Computer#s final hand: {comp_card}, final score. {comp_card}")
    print("You went over. You lose")


def computer_card():
    global comp_card
    comp_card = random.choice(c)
    print(f"Computer's first card: {comp_card}")


def adding_comp_card():
    if sum(comp_card) < 17:
        comp_card.append(random.choice(c))
        print(f"Computer's final hand: {card}, final score: {sum(comp_card)}")
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
