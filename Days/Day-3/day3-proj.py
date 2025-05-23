print("Welcome to Treasure Island")
print("Your mission is to find treasure.")
print("You're at a cross road. Where do you want to go?")

cross_road = input("Type left or right: ")

if cross_road == "left":
    print("Correct Path")
    input("Would you like to swim or wait? ")
elif cross_road == "right":
    print("You fell into a trap and died. Game Over...")
else:
    print("Please follow instructions next time.")