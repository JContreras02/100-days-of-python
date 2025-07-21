import art
print(art.logo)

# Operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

operators_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Function for calculation will keep going until loop is false
def calculator():
    should_continue = True
    num1 = float(input("What's your first number?: "))

    while should_continue:
        for symbol in operators_dict:
            print(symbol)
        operator = input("Pick an operator: ")

        if operator not in operators_dict:
            print("Invalid operator. Try again.")
            continue

        num2 = float(input("What's the next number?: "))
        result = operators_dict[operator](num1, num2) 
        print(f"{num1} {operator} {num2} = {result}")
        next_step = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation. ").lower()

        if next_step == 'y':
            num1 = result
            print("\n" * 3)
        elif next_step == 'n':
            print("\n" * 20)
            should_continue = False
        else:
            print("Goodbye!")
            return

calculator()