import random

def RPS():
    print("Let's play Rock, Paper, Scissors!")
    
    choices = ["rock", "paper", "scissors"]

    random.shuffle(choices)
    botchoice = choices[0]
    userchoice = input("What option are you throwing? ")

    if userchoice == botchoice:
        print("Jinx! Retry.")
    if userchoice not in "rock, paper, scissors":
        print("Invalid string. Try again!")

    if userchoice.lower() == "rock" and botchoice == "paper":
        print("Paper! You lose! Retry.")
    if userchoice.lower() == "rock" and botchoice == "scissors":
        print("Scissors! You win!")

    if userchoice.lower() == "paper" and botchoice == "scissors":
        print("Scissors! You lose! Retry.")
    if userchoice.lower() == "paper" and botchoice == "rock":
        print("Rock! You win!")

    if userchoice.lower() == "scissors" and botchoice == "rock":
        print("Rock! You lose! Retry.")
    if userchoice.lower() == "scissors" and botchoice == "paper":
        print("Paper! You win!")


if __name__ == "__main__":
    RPS()
