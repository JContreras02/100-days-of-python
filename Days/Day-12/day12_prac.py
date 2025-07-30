game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# Block scope(not in python), local scope, global scope prac.

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    # local scope, can only be accessed inside of function
    print(new_enemy)

# variable is not defined since it is not reference in a global scope
print(new_enemy)