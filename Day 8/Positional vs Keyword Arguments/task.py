# Functions with input

"""def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")"""


def greet(name, loc):
    print(f"Hello {name}")
    print(f"Welcome to our {loc}")


# positional argument
greet("Anitha", "India")

# keyword argument
greet(name="Anitha", loc="India")
greet(loc="Tamil", name="Germany")  # even when we change the argument order, value will be picked correctly


def cal(a, b):
    c = a + b
    print(f"Total is {c}")


cal(5, 3)
cal(a=5, b=3)
cal(b=3, a=5)  # even when we change the argument order, value will be picked correctly

print("LOVE CALCULATOR")


def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true = name1 + name2
    t = 0
    r = 0
    u = 0
    e1 = 0
    l = 0
    o = 0
    v = 0
    e2 = 0
    total1 = 0
    total2 = 0
    for letters in true:
        if letters == "t":
            t += 1
        if letters == "r":
            r += 1
        if letters == "u":
            u += 1
        if letters == "e":
            e1 += 1
        total1 = t + r + u + e1

    for letters in true:
        if letters == "l":
            l += 1
        elif letters == "o":
            o += 1
        elif letters == "v":
            v += 1
        elif letters == "e":
            e2 += 1
        total2 = l + o + v + e2

    print(f"{total1}{total2}")


calculate_love_score("Kanye West", "Kim Kardashian")

# counting the character with count() function
name = "Kanye West"
name = name.lower()
total = name.count('t')
print(total)
