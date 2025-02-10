import random

play = "Y"

while play != "N":

    comp = random.randint(1,3)

    if comp == 1:
        choice = "rock"
    elif comp == 2:
        choice = "paper"
    else:
        choice = "scissors"

    print("Start Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    num = input("What do you want to throw?")
    num = int(num)

    if num == 1:
        mychoice = "rock"
    elif num == 2:
        mychoice = "paper"
    else:
        mychoice = "scissors"

    print("Computer:", choice, "vs you:", mychoice)

    if choice == mychoice:
        print("it is a tie!")
    elif choice == "rock" and mychoice == "paper":
        print("You win!!")
    elif choice == "paper" and mychoice == "scissors":
        print("You win!!")
    elif choice == "scissors" and mychoice == "rock":
        print("You win!!")
    else:
        print("you lost!")

    play = input("Do you want to play again? (Y/N):").upper()