from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    end_of_calculation = False
    operation_symbol = input("Pick up and operation symbol from the line above: ")
    num2 = float(input("What's the next number?: "))

    # Calling the function that matches the operation chosen by user.
    first_answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    while not end_of_calculation:
        user_decision = input(
            f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit : ").lower()
        if user_decision == "y":
            operation_symbol = input("Pick up and operation symbol from the line above: ")
            num3 = float(input("What's the next number?"))
            second_answer = operations[operation_symbol](first_answer, num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
            first_answer = second_answer
        else:
            end_of_calculation = True
            calculator()


calculator()
