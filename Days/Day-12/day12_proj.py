from game_art import logo
import random

print(logo)

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

print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
rand_num = random.randint(1,100)

if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} remaining to guess the number.\n")
    game_logic(rand_num, attempts)
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} remaining to guess the number.\n")
    game_logic(rand_num, attempts)



