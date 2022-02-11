# Write a program that generates a random number between 1 and 10 and lets
# the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
import time

print("Let's play a little game")
print("I guessed a number from 1 to 10. Try to guess it ")
print("Please insert number from 1 to 10 : ")
player_number = int(input(" "))
guess_number = random.randint(1, 10)
while player_number != guess_number:
    print("Give me a few second...")
    time.sleep(0.5)
    print("You're wrong.")
    print("I riddled a new number, and you try again.")
    print("Please insert number from 1 to 10 : ")
    guess_number = random.randint(1, 10)
    player_number = int(input(" "))
if player_number == guess_number:
    print("Give me a few second...")
    time.sleep(0.5)
    print("Yoy are luky.")
