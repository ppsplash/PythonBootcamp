import random
from art import logo


def user_card():
    card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Your cards: {card}, current score: {sum(card)}")


def computer_card():
    card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Computer's first card: {card[0]}")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if start == 'y':
    print(logo)
    user_card()
    computer_card()
    next = input("Type 'y' to get an another card, type 'n' to pass: ").lower()
