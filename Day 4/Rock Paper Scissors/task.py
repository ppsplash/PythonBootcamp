import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____0
          ______)
       __________)
      (____)
---.__(___)
'''
choice=['rock','paper','scissors']
print("Welcome to the Game: Rock Paper Scissors. Lets have fun!!")
User_choice=int(input("What do you choose: Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice =random.randint(0,2)
print(f"Computer chose: {choice[computer_choice]}")
if User_choice == computer_choice :
    print("Its a draw. Please play again")
elif User_choice == 0 and computer_choice == 1:
    print("Computer wins")
elif User_choice == 0 and computer_choice == 2:
    print("User wins")
elif User_choice == 1 and computer_choice == 2:
    print("Computer wins")
elif User_choice == 1 and computer_choice == 0:
    print("User wins")
elif User_choice == 2 and computer_choice == 1:
    print("Computer wins")
elif User_choice == 2 and computer_choice == 0:
    print("Computer wins")
else:
    print("Please enter valid numbers such as 0,1,2")



