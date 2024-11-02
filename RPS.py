import random

#is a list of choics the cpu can make, and intializes the counter that will track the consecutive wins
cpuChoices = ["rock", "paper", "scissors"]
counter = 0
#until the program ends the user will choose rock, paper or scissors and so will the ai
while(1):
    #user and AIs choice
    userChoice = input("Choose either rock, paper, or scissors\n")
    cpuChoice = random.choice(cpuChoices)

    #when draw happens    
    if(userChoice == cpuChoice):
        print("Computer chooses ", cpuChoice, "\nThere is a tie!")
        print("Winstreak:", counter)
    #when user wins
    elif((userChoice == "rock" and cpuChoice == "scissors") or (userChoice == "paper" and cpuChoice == "rock") or (userChoice == "scissors" and cpuChoice == "paper")):
        print("Computer chooses ", cpuChoice, "\nYou Won!")
        counter = counter+1
        print("Winstreak:",counter)
    #when ai wins
    else:
        print("Computer chooses ", cpuChoice, "\nYou Lose!")
        counter = 0
        print("Winstreak:",counter)
