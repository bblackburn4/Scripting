import random
import math
import os

#Definisons for the game
def mainmenue(): #is the def for the main menue in the game
    print('\tWelcome to Guess the number by Bryon Blackburm.\n')
    print("Here you will get to set the number ramge you want")
    print('Based on your range will set how menny guesses you will get')
mainmenue()
# Script Varables
lower = int(input("Emter Lower bound:- ")) 
upper = int(input("Enter Upper bound:- ")) 
x = random.randint(lower, upper) # generating random number between
count = 0 # Initializing the number of guesses.
clearscreen = os.system('clear')

print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
clearscreen
#in game logic
while count < math.log(upper - lower + 1, 2):
    count += 1
        
        # taking guessing number as input
    guess = int(input("Guess a number:- ")) 

        # Condition testing
    if x == guess:
        print("Congratulations you did it in ", count, 'trys')
        # Once guessed, loop will break 
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses will display below.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d"%x)

#Limit varables in this script to this script.
if __name__ == "__main__":
    pass