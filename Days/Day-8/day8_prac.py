'''
def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(20)
'''

def greet_with(name, location):
    print(f"Hello {name} from {location}, its a pleasure to meet you!")

name = input("Hello! What's your name? ")
location = input("Where are you located? ")
greet_with(name, location)