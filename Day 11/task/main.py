import random
from art import logo

c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def user_card():
    global my_card
    my_card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    print(f"Your cards: {my_card}, current score: {sum(my_card)}")


def adding_cards():
    next = input("Type 'y' to get an another card, type 'n' to pass: ").lower()
    while next == 'y':
        my_card.append(random.choice(c))
        print(f"Your cards: {my_card}, current score: {sum(my_card)}")
        next = input("Type 'y' to get an another card, type 'n' to pass: ").lower()
    while next == 'n' and sum(comp_card) < 17:
        comp_card.append(random.choice(c))
        print(f"Your final hand: {my_card}, final score: {sum(my_card)}")
        print(f"Computer's final hand: {comp_card}, final score. {comp_card}")


def not_adding_cards():
    print(f"Your final hand: {my_card}, final score: {sum(my_card)}")
    print(f"Computer's final hand: {comp_card}, final score. {comp_card}")
    print("You went over. You lose")


def computer_card():
    global comp_card
    comp_card = random.choice(c)
    print(f"Computer's first card: {comp_card}")


def adding_comp_card():
    if sum(my_card) == 21 and my_card == [10, 11]:
        print(f"Your final hand: {my_card}, final score: 0 ")
        print(f"Computer's final hand: {comp_card}, final score. {comp_card}")
        print("Win with a Blackjack")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if start == 'y':
    print(logo)
    user_card()
    computer_card()
    while sum(my_card) < 21:
        adding_cards()
    if sum(my_card) > 21:
        not_adding_cards()
    if sum(my_card) == 21:
        adding_comp_card()
