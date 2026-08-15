"""
Implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""


import random

while True:
        try:
            level = int(input("Level: "))
            if level > 0: break
        except ValueError:
            pass

random_value = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0: continue

        if guess < random_value:
            print("Too small!")
        elif guess > random_value:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
         pass
