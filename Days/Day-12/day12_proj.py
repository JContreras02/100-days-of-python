from game_art import logo
import random

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game_logic(rand_num, attempts):
    guess = int(input("Make a guess: "))
    if guess == rand_num:
        print(f"You got it! The answer was {rand_num}.")
    elif guess > rand_num:
        while attempts != 0:
            attempts -= 1
            print(f"Too high. Guess Again.")
            print(f"You have {attempts} attempts remaining to guess the number.\n")
            game_logic(rand_num, attempts)
        print(f"You've run out of guesses. The number was {rand_num}.")
        print("Please re-run the code to play again!")
    elif guess < rand_num:
        while attempts != 0:
            attempts -= 1
            print(f"Too low. Guess Again.")
            print(f"You have {attempts} attempts remaining to guess the number.\n")
            game_logic(rand_num, attempts)
        print(f"You've run out of guesses. The number was {rand_num}.")
        print("Please re-run the code to play again!")
    else:
        while attempts != 0:
            attempts -= 1
            print(f"Guess Again.")
            print(f"You have {attempts} attempts remaining to guess the number.\n")
            game_logic(rand_num, attempts)
        print(f"You've run out of guesses. The number was {rand_num}.")
        print("Please re-run the code to play again!")



def set_difficulty():
    """Sets either easy or hard difficulty."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS



print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")

rand_num = random.randint(1,100)
turns = set_difficulty()

print(f"You have {turns} remaining to guess the number.\n")

guess = int(input("Make a guess: "))

