import random
from art import logo

c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def user_card():
    global my_card
    global total
    my_card = random.sample([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], 2)
    total = sum(my_card)
    print(f"Your cards: {my_card}, current score: {total}")


def computer_card():
    global comp_card
    comp_card = random.choice(c)
    print(f"Computer's first card: {comp_card}")


def adding_usercards():
    my_card.append(random.choice(c))
    total = sum(my_card)
    print(f"Your cards: {my_card}, current score: {total}")
    print(f"Computer's first card: {comp_card}")
    if total > 21 and my_card != [11]:
        print("You went over. You lose :(")
        exit()


def adding_compcards():
    while sum(comp_card) != 17:
        comp_card.append(random.choice(c))
    print(f"Your final hand: {my_card} , final score : {total}")
    print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")
    if sum(comp_card) > 21:
        print("Opponent went over. You win:)")
    elif sum(comp_card) < 21 and sum(comp_card) > total:
        print("Opponent win")
    elif sum(comp_card) < 21 and sum(comp_card) == total:
        print("Draw")
    elif sum(comp_card) < 21 and total > sum(comp_card):
        print("You went over. Opponent win!!")


def validation(total):
    if total == 21 and my_card == [11]:
        print(f"Your final hand: {my_card} , final score : {total}")
        print(f"Computer's final hand: {comp_card} , final score : {sum(comp_card)}")
        print("Win with a Blackjack:)")
    if total > 21 and my_card == [11]:
        my_card.remove[11]
        my_card.append[1]
        total = sum(my_card)
        print(f"Your cards: {my_card}, current score: {total}")


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if start == 'y':
    print(logo)
    user_card()
    computer_card()
    validation(total)
    repeat = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
    if repeat == 'y':
        adding_usercards()
        if total == 21 and my_card == [11]:
            print("You have won with Blackjack:)")
        if total > 21 and my_card == [11]:
            my_card.remove[11]
            my_card.append[1]
            total = sum(my_card)
            print(f"Your cards: {my_card}, current score: {total}")
        if total == 21:
            print(f"Type 'y' to get another card, type 'n' to pass: ")

        if total < 21:
            ans = input(f"Type 'y' to get another card, type 'n' to pass: ").lower()
            if ans == 'y':
                adding_usercards()

            else:
                adding_compcards()

        if total > 21 and my_card != [11]:
            print("You went over. You lose :(")

    while repeat == 'n':
        adding_compcards()
        exit()
