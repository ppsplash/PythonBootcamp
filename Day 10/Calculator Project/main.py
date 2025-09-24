from art import logo

print(logo)


def add(n1, n2):
    output = n1 + n2
    print(output)


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


n1 = input("Whats the first number")
print("+\n-\n*\n/\n")
operation = input("Pick an operation")
n2 = input("Whats the next number")
if operation == '+':
    add(n1, n2)
if operation == '-':
    n3 = subtract(n1, n2)
    print(n3)
if operation == '*':
    n3 = multiply(n1, n2)
    print(n3)
if operation == '/':
    n3 = division(n1, n2)
    print(n3)
