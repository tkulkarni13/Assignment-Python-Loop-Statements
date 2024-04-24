import random

# Task 1: Random Choice Game

options = ["rock", "paper", "scissors"]
user_answer = input("Pick from rock, paper, or scissors: ")
bot_answer = random.choice(options)
if (user_answer == "rock"): # all scenarios when user picks rock
    if (bot_answer == "scissors"):
        print("The bot picked scissors. You won!")
    elif (bot_answer == "paper"):
        print("The bot picked paper. You lost.")
    elif (bot_answer == "rock"):
        print("The bot picked rock. It was a draw.")
elif (user_answer == "paper"): # all scenarios when user picks paper
    if (bot_answer == "scissors"):
        print("The bot picked scissors. You lost.")
    elif (bot_answer == "paper"):
        print("The bot picked paper. It was a draw")
    elif (bot_answer == "rock"):
        print("The bot picked rock. You won!")
elif (user_answer == "scissors"): # all scenarios when user picks scissors
    if (bot_answer == "scissors"):
        print("The bot picked scissors. It was a draw.")
    elif (bot_answer == "paper"):
        print("The bot picked paper. You won!")
    elif (bot_answer == "rock"):
        print("The bot picked rock. You lost.")
else: # if the user inputs an unexpected answer
    print("You didn't pick rock, paper, or scissors")