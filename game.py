#rock paper scissors game

import random

user_input = input("Pick an option: Rock, Paper, Scissors): ")
actions = ["rock", "paper", "scissors"]
computer_action = random.choice(actions)

print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

# checking for invalid inputs
if user_input not in actions:
    print(f"\ninvalid option! try again")
else:    
    if user_input == computer_action:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper folds rock! You lose.")
    elif user_input == "paper":
        if computer_action == "rock":
            print("Paper folds rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
    else:
            print("Rock smashes scissors! You lose.")

