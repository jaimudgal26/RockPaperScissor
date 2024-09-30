import random

# ascii_images=[rock, papper, scissors]
userInput = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
computer_choice = random.randint(0, 2)
print(computer_choice)

if userInput >= 3 or userInput < 0:
  print("You typed an invalid number, you lose!")
elif userInput == 0 and computer_choice == 2:
  print("You win!")
elif userInput == 2 and computer_choice == 0:
  print("You lose!")
elif computer_choice > userInput:
  print("You lose!")
elif userInput > computer_choice:
  print("You win!")
elif computer_choice == userInput:
  print("It's a tie!")
