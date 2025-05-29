import random

# ascii art for rock, paper, scissors game
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]

#logic
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player >= 0 and player <= 2:
    print(game_images[player])

computer = random.randint(0,2)
print("Computer chose:")
print(game_images[computer])

if player >= 3 or player < 0:
    print("You typed an invalid number. You lose!\n")
elif player == 0 and computer == 2:
    print("You Win!\n")
elif computer == 0 and player == 2:
    print("You Lose!\n")
elif computer > player:
    print("You Lose!\n")
elif player > computer:
    print("It's a Win!\n")
elif player == computer:
    print("It's a Draw!\n")

  