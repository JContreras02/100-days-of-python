import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

number_1 = float(input("What's your first number?: "))
operator_list = "+-*/"
for char in operator_list:
    print(char)
operator = input("Pick an operator: ")
number_2 = float(input("What's the next number?: "))

print(f"{number_1} {operator} {number_2} = {operators_dict[operator](number_1, number_2)}")

# Program asks the user to type the first number.
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# Program asks the user to type the second number.
# Program works out the result based on the chosen mathematical operator.
# Program asks if the user wants to continue working with the previous result.
# If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# Add the logo from art.py