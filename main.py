import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User's action
user_action = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_action == 0:
  print(rock)
if user_action == 1:
  print(paper)
if user_action == 2:
  print(scissors)

# Computer's action
print("Computer chose:")
computer_action = random.randint(0, 2)
if computer_action == 0:
  print(rock)
if computer_action == 1:
  print(paper)
if computer_action == 2:
  print(scissors)

# Compare actions
if user_action == computer_action:
  print("Draw")
elif user_action - computer_action == 1:
  print("You win")
elif user_action - computer_action == -2:
  print("You win")
elif user_action > 2 or user_action < 0:
  print("Invalid number, You lose")
else:
  print("You lose")
