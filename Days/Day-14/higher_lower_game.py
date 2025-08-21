from art import logo, vs
from game_data import data
import random

def format_data(data):
    data_name = data["name"]
    data_desc = data["description"]
    data_country = data["country"]
    return f"{data_name}, {data_desc}, from {data_country}"

print(logo)

data_a = random.choice(data)
data_b = random.choice(data)
if data_a == data_b:
    data_b = random.choice(data)
    



print(f"Compare A: {format_data(data_a)}.")
print(f"Compare B: {format_data(data_b)}.")


guess = input("Who has more followers? Type 'A' or 'B': ")