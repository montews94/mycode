#!/usr/bin/env python3
#if logic challenge: Rock, Paper, Scissors

# import random for computer picks
import random
#challenge player to a game
print()
print(" Let's play rock, paper, scissors.")
print("----------------------------------")
#create a while loop
while True:
    #prompt for user input
    user_input= input("Please enter Rock, Paper, or Scissors: ").strip().lower()
    print()
    
    print("You have selected: ", user_input)
    print()#adding space
    # change random integers into human language
    computer_input= random.randint(0, 2)
    if computer_input == 0 :
        computer_choice= "rock"

    elif computer_input == 1 :
        computer_choice= "paper"

    elif computer_input == 2 :
        computer_choice= "scissors"

    print("And computer chooses: ", computer_choice)
    print()#adding space
    #enter win/loss scenarios
    if user_input == "rock" and computer_choice == "rock":
        print("You both chose rock? Thats a tie!")
        break
    elif user_input == "rock" and computer_choice == "paper":
        print("Paper covers rock! You Lose!")
        break
    elif user_input == "rock" and computer_choice == "scissors":
        print("Rock smashes scissors! You Win!")
        break
    if user_input == "paper" and computer_choice == "rock":
        print("Paper covers rock! You Win!")
        break
    elif user_input == "paper" and computer_choice == "paper":
        print("You chose paper? Thats a Tie!")
        break
    elif user_input == "paper" and computer_choice == "scissors":
        print("Scissors cuts paper! You Lose!")
        break
    if user_input == "scissors" and computer_choice == "rock":
        print("Rock smashes scissors! You Lose!")
        break
    elif user_input =="scissors" and computer_choice == "paper":
        print("Scissors cuts paper! You Win!")
        break
    elif user_input == "scissors" and computer_choice == "scissors":
        print("You chose scissors? Thats a Tie!")
        break
    # if anything beside rock, paper, or scissors is input
    else:
        print("Was that a valid input? Try again")

