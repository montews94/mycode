#!/usr/bin/env python3
#if logic challenge: Rock, Paper, Scissors

# import random for computer picks
import random
#challenge player to a game
print(" Let's play rock, paper, scissors.")
#create a while loop

# this looks good!!! let me help you out a bit:

while True:
    
    # good user input normalization
    user_input= input("Please enter Rock, Paper, or Scissors: ").strip().lower()
    
    print("You have selected: ", user_input)

    computer_input= random.randint(0, 2)
    
    if computer_input == 0:
        computer_choice= "rock"

    elif computer_input == 1:
        computer_choice= "paper"

    elif computer_input == 2:
        computer_choice= "scissors"

    print("And computer chooses: ", computer_choice)
    
    if user_input == "rock" and computer_choice == "paper":
        print("You win!")

    # you get the idea-- now if you have the different possible combinations, you can finish this up no problem
    # just some syntax stuff that needed cleaned above, everything else looks great!

    
    break
