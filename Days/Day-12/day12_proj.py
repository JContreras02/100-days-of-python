from game_art import logo
import random

print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, rand_num, turns):
    """Checks answer with guess and returns num of turns remaining."""
    print("\n")
    if guess == rand_num:
        print(f"You got it! The answer was {rand_num}.")
    elif guess > rand_num:
        print(f"Too high.")
        return turns - 1
    elif guess < rand_num:
        print(f"Too low.")
        return turns - 1
    else:
        print(f"Invalid answer.")

def set_difficulty():
    """Sets either easy or hard difficulty."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100.\n")

    rand_num = random.randint(1,100)
    turns = set_difficulty()

    print(f"You have {turns} remaining to guess the number.\n")

    guess = 0
    while guess != rand_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, rand_num, turns)
        if turns == 0:
            print(f"You've run out of guesses. The number was {rand_num}.")
            print("Please re-run the code to play again!\n")
            return
        elif guess != rand_num:
            print("Guess Again.\n")

game()