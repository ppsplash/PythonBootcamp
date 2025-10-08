from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


def repeated_calculation(n1):
    operation = input("Pick an operation ")
    n2 = int(input("Whats the next number: "))
    if operation == '+':
        n3 = add(n1, n2)
        print(n3)
    elif operation == '-':
        n3 = subtract(n1, n2)
        print(n3)
    elif operation == '*':
        n3 = multiply(n1, n2)
        print(n3)
    elif operation == '/':
        n3 = division(n1, n2)
        print(n3)
    print(f"{n1}{operation}{n2} = {n3}")
    return n3


def calculator():
    n1 = int(input("Whats the first number: "))
    print("+\n-\n*\n/\n")
    output = repeated_calculation(n1)
    repeat = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    if repeat == 'y':
        repeated_calculation(output)
    else:
        print("\n" * 20)
        calculator()


calculator()
