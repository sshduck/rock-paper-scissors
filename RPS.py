import random

class Choices:
    def __init__(self, userchoice, botchoice):
        self.userchoice = userchoice.lower()
        self.botchoice = botchoice

    def check(self):
        if self.userchoice == self.botchoice:
            print("Jinx! Retry.")
        if self.userchoice not in "rock, paper, scissors":
            print("Invalid string. Try again!")

        if self.userchoice.lower() == "rock" and self.botchoice == "paper":
            print("Paper! You lose! Retry.")
        if self.userchoice.lower() == "rock" and self.botchoice == "scissors":
            print("Scissors! You win!")

        if self.userchoice.lower() == "paper" and self.botchoice == "scissors":
            print("Scissors! You lose! Retry.")
        if self.userchoice.lower() == "paper" and self.botchoice == "rock":
            print("Rock! You win!")

        if self.userchoice.lower() == "scissors" and self.botchoice == "rock":
            print("Rock! You lose! Retry.")
        if self.userchoice.lower() == "scissors" and self.botchoice == "paper":
            print("Paper! You win!")



def RPS():
    print("Let's play Rock, Paper, Scissors!")
    
    choices = ["rock", "paper", "scissors"]

    botchoice = random.choice(choices)
    userchoice = input("What option are you throwing? ").strip()

    go = Choices(userchoice, botchoice)
    go.check()

   
if __name__ == "__main__":
    RPS()
