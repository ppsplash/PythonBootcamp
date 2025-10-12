import random
from art import logo


def user_card():
    global card
    card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Your cards: {card}, current score: {sum(card)}")


def adding_cards():
    global c
    c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card.append(random.choice(c))
    print(f"Your cards: {card}, current score: {sum(card)}")
    if sum(card) > 21:
        print(f"Your final hand: {card}, final score: {sum(card)}")
        print(f"Computer#s final hand: {comp_card}, final score. {comp_card}")
        print("You went over. You lose")


def computer_card():
    global comp_card
    comp_card = random.choice(c)
    print(f"Computer's first card: {comp_card}")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if start == 'y':
    print(logo)
    user_card()
    computer_card()
    next = input("Type 'y' to get an another card, type 'n' to pass: ").lower()
    if next == 'y':
        adding_cards()
        computer_card()
