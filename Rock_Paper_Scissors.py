#Rock, Paper, Scissor Game

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

#Write your code below this line 👇
choices = [rock, paper, scissors]
choices_words = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.  "))
computer_choice = random.randint(0,2)



  

#How player wins:
if player_choice <= 2 and player_choice >= 0:
    print(f"You chose {choices_words[player_choice]}: ")
    print(choices[player_choice])

    print(f"The computer chose {choices_words[computer_choice]}:")
    print(choices[computer_choice])
    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == 0 and computer_choice == 2:
        print("You won!")
    elif player_choice == 1 and computer_choice == 0:
        print("You won!")
    elif player_choice == 2 and computer_choice == 1:
        print("You won!")
    else:
        print("Sorry, you lost.")
else:
    print("You chose an invalid number. You lose.")