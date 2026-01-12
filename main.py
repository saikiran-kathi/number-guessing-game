# Number Guessing Game

import random

print("Welcome to Number Guessing Game")
print("I am thinking of a number between 1 and 10")

secret_number = random.randint(1, 10)

guess = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
