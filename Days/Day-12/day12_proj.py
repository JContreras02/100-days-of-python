from game_art import logo
import random

print(logo)

def game_logic(diff_level):
    return



print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower
random_number = random.randint(1,100)

if difficulty == "easy":
    attempts = 10

elif difficulty == "hard":
    attempts = 5
else:
    print("Please enter a difficulty. Try Again")



