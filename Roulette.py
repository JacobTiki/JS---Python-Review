import random
import time

def generateWheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spinWheel(spaces):
    return random.choice(spaces)

def playGame():
    spaces = generateWheel()
    money = 1000
    while True:
        print("You have $" + str(money))
        bet = input("How much money will you bet? ")
        bet = int(bet)
        color = input("What color are you betting on? ")
        print("The wheel is spinning......")
        time.sleep(4)

        landed = spinWheel(spaces)
        print("It landed on " + landed)
        if color == landed:
            money += bet
            print("Congratulations! You now have $" + str(money))
        else:
            money -= bet
            print("Sorry! You now have $" + str(money))
        if(money <= 0):
            print("Please leave the casino")
            break
        playAgain = input("Do you want to play again? ")
        if(playAgain == "no"):
            break

playGame()