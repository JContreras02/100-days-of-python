from art import logo, vs
from game_data import data
import random

def format_data(data):
    """Function to format all the game data into a printable format."""
    data_name = data["name"]
    data_desc = data["description"]
    data_country = data["country"]
    return f"{data_name}, {data_desc}, from {data_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Takes user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        if user_guess == "a":
            return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
should_game_cont =  True
data_b = random.choice(data)
score = 0

while should_game_cont:
    data_a = data_b
    data_b = random.choice(data)
    if data_a == data_b:
        data_b = random.choice(data)
        
    print(f"Compare A: {format_data(data_a)}.")
    print(vs)
    print(f"Compare B: {format_data(data_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count = data_a["follower_count"]
    b_follower_count = data_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"Your correct! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        should_game_cont = False