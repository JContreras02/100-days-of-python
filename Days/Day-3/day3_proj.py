print("Welcome to Treasure Island")
print("Your mission is to find treasure.\n")
print("You're at a cross road. Where do you want to go?")

cross_road = input("Type left or right: ").lower()
correct = "Correct Path!\n"
unknown_answer = "Game Over. Please follow instructions next time.\n"
ascii_art = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

if cross_road == "left":
    print(correct)
    swim_wait = input("Would you like to swim or wait for a boat? \n").lower()
    if swim_wait == "wait":
        print(correct)
        door = input("Now pick a door, blue, red, yellow. \n").lower()
        if door == "yellow":
            print(correct)
            print("You have now found the Treasure! YOU WIN!")
            print(ascii_art)
        elif door == "blue":
            print("You set off a bomb! Game Over...")
        elif door == "red":
            print("You caught on fire! Game Over...")
        else:
            print(unknown_answer)
    elif swim_wait == "swim":
        print("You swam and got ate by sharks. Game Over...")
    else:
        print(unknown_answer)
elif cross_road == "right":
    print("You fell into a trap and died. Game Over...\n")
else:
    print(unknown_answer)