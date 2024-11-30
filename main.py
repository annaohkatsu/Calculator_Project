import art
print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": devide
}


continue_cal = True
n1 = float(input("Type the first number: "))
result = n1

while continue_cal:
    choice = input('Type a mathematical operator from +,-, *, /: ')
    n2 = float(input("Type the second number: "))

    result = operation[choice](result,n2)
    print(result)
    continue_cal = input(f"Do you want to continue with {result}? yes or no: ").lower()
    if continue_cal == "no":
        continue_cal = False
        print("\n"*50)
    elif continue_cal == "yes":
        continue_cal = True
        