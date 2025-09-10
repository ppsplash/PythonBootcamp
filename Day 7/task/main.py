import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.


"""word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_" """

"""correct_letters = []

while lives < 6
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            lives = lives
            print(stages[lives])
        elif letter in correct_letters:
            display += letter
            lives = lives
            print(stages[lives])
        else:
            display += "_"
            lives -= 1"""
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
l = len(chosen_word)
placeholder = "_" * l
print(f"Word to guess: {placeholder}")

while not lives == 0:
    guess = input("Guess a letter: ".lower())
    output = ""
    appeared_letters = ""
    if guess in chosen_word:
        output += guess
        print(f"You guessed {guess}. Thats in the word.")
        print(output)
        print(stages[lives])
        appeared_letters += guess
        print(f"*************************************You have {lives}/6 lives left******************************")
    else:
        output += "_"
        lives += 1
        print(f"You guessed {guess}. Thats not in the word. You lose a life")
        print(output)
        print(stages[lives])
        print(f"*************************************You have {lives}/6 lives left******************************")

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
