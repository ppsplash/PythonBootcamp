print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
percentage= tip/100+1
amount= round(bill*percentage/people,2)
print(f"Each person should pay: ${amount}") # data type conversion to print with help of "f string and paranthesis"
print("Each person should pay: $"+ str(amount)) # another way to display datatype with conversion to string



