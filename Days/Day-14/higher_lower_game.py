from art import logo, vs
from game_data import data
import random

def random_generation():
    """Return a random piece of data from the list."""
    return random.choice(data)

def data_comparison():
    return

print(logo)

choice_a = random_generation()
choice_b = random_generation()

print(choice_a['name'])
print(choice_b)