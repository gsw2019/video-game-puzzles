"""
File:           main.py
Author:         Garret Wilson
Date:           06/24/25
Description:    Handles all I/O
"""

import access_override_puzzles_solver as solver


def get_integer_input():
    """Ensures user input is an integer. Continues to prompt user until
    an integer is entered or program is interrupted.

    :return:    (int) target value
    """
    while True:
        try:
            return int(input("Target: "))
        except ValueError:
            print("Error: Invalid input. Target must be an integer")


def main():
    """Prompts the user to choose the access override puzzle 2 solver
    or the access override puzzle 3 solver. Continues to prompt user
    until a valid input is provided or program is interrupted.

    :return:    None
    """
    while True:
        puzzle_choice = input("Access override puzzle 2 solver (p2) or access "
                              "override puzzle 3 solver (p3)? ")

        if puzzle_choice.lower() == "p2":
            target = get_integer_input()
            result = solver.puzzle_2(target)

            if result:
                print("-------------------------")
                print(result)
            else:
                print(f"No solution found for target: {target}")
            break

        if puzzle_choice.lower() == "p3":
            target = get_integer_input()
            result = solver.puzzle_3(target)

            if result:
                print("-------------------------")
                print(result)
            else:
                print(f"No valid sets found for target: {target}")
            break

        else:
            print("Error: Mut enter 'p2' or 'p3'")


if __name__ == "__main__":
    main()
