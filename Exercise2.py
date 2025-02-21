import random

random_num = random.randint(1,100)
guesses = 0
while True:
    guess = int(input("Guess a number \n"))
    if guess > random_num:
        print("Guess lower")
    elif guess < random_num:
        print("Guess higher")
    else:
        print("Congratulations! You guessed the number.")
        break
    guesses += 1
print("It took you " + str(guesses + 1) + " guesses to guess the number.")