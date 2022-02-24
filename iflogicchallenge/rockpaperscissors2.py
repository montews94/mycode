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
    if user_input != "rock" or "paper" or "scissors":
        print("Was that a valid input? Try again")
    else:
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
    elif user_input == "rock" and computer_choice == "paper":
        print("Paper covers rock! You Lose!")
    elif user_input == "rock" and computer_choice == "scissors":
        print("Rock smashes scissors! You Win!")
    if user_input == "paper" and computer_choice == "rock":
        print("Paper covers rock! You Win!")
    elif user_input == "paper" and computer_choice == "paper":
        print("You chose paper? Thats a Tie!")
    elif user_input == "paper" and computer_choice == "scissors":
        print("Scissors cuts paper! You Lose!")
    if user_input == "scissors" and computer_choice == "rock":
        print("Rock smashes scissors! You Lose!")
    elif user_input =="scissors" and computer_choice == "paper":
        print("Scissors cuts paper! You Win!")
    elif user_input == "scissors" and computer_choice == "scissors":
        print("You chose scissors? Thats a Tie!")
    # ask user if they want to play again
    play_again= input("Want to play again(y/n)?: ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
