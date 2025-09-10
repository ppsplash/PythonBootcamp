print('''
                                                                           
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
              88           88                                 88  
              ""           88                                 88  
                           88                                 88  
 ,adPPYba,    88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88    88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP"""""""    88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa    88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"'    88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
                                                               
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
way=str(input("Which way you would love to go - left or right. "
              "PLease enter 'L' for left and 'R' for right")).lower()
if way=='r':
    print("You are out.Its an pit and dead End :(:(")
else:
    print("There is an lake to cross.Would you like to swim & cross OR wait for Boat\n")
    option=str(input("Please enter 'S' to Swim amd cross and 'B' to Boat ")).lower()
    if option=='b':
        Boat=str(input("There are two Boats :Blue and Red. Which one would you like to Board. "
                       "Please enter 'Y' for Yellow and 'R' for Red")).lower()
        if Boat == 'y':
            print("YOU WIN!!!!You\'ve boarded a right boat to Treasure Island... HOOORRAAYYYYY")
        else:
            print("Sorry,you\'re haunted by ghosts and you will never get an Treasure :(:( ")
    else:
        print("Sorry,you\'re haunted by ghosts and you will never get an Treasure :(:( ")





