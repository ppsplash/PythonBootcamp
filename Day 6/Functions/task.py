# Husband gave task to print months of year
# no = int(input("please enter from which month,we should print it out"))
"""month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']
total = len(month)"""

### while no <= total:
#    print(f"Months are :{month[no - 1]}")
#  no += 1
"""no -= 1
if no == 0:
    print(f"Months are {month[0], month[1], month[2], month[3]}")
elif no == 1:
    print((f"Months are {month[1], month[2], month[3]}"))
elif no == 2:
    print((f"Months are {month[2], month[3]}"))
elif no == 3:
    print((f"Months are {month[3]}"))"""

"""if (no <= total):
    no -= 1
    while (0 <= no < 12):
        print(f"Months are :{month[no]}")
        no += 1
else:
    print("Please enter valid no")"""
"""
if (no <= 1):
    print("Janaury")
if (no <= 2):
    print("Feb")
if (no <= 3):
    print("Mar")
if (no <= 4):
    print("Apr")
if (no <= 5):
    print("May")
"""


def add(x, y):
    total = x + y
    print(f"The total sum is {total}")


a = input("Please enter 'A' value to add\n")
b = input("Please enter 'B' value to add\n")
l = int(a)
m = int(b)
add(l, m)
