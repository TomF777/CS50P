"""
Implement a program that:

 - Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
 - Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits.
   No need to support operations other than addition (+).

 - Prompts the user to solve each of those problems.
   If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
   allowing the user up to three tries in total for that problem.
   If the user has still not answered correctly after three tries, the program should output the correct answer.

 - The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

import random


def main():

    level = get_level()
    score = 0

    for iter in range(0, 10):

        num_01 = generate_integer(level)
        num_02 = generate_integer(level)

        for _ in range(3):
            try:
                user_sum = int(input(f"{num_01} + {num_02} = "))
                if user_sum == int(num_01) + int(num_02):
                    score += 1
                    break
            except ValueError:
                pass

            print("EEE")

        else:
            # show correct answer if 'for loop' not interrupted by 'break'
            print(f"{num_01} + {num_02} = {num_01 + num_02}")

    # print total score
    print(f"Score: {score}")


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
