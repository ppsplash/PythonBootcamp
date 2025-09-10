print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill=5
        print("Child ticket is $5.")
    elif age >=12 and age <18:
        bill=7
        print("Youth ticket is $7.")
    else:
        bill=12
        print("Adult ticket is $12.")
    photo=input("Do wou want photos: please enter Y for Yes and N or No")
    if photo == "Y":
        bill +=3
        print(f"Your ticket price with photo taken will be ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
