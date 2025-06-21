"""
File:       access_override_puzzles_solver.py
Author:     Garret Wilson
Purpose:    provides possible inputs to Access Override Puzzle #2 and
            Access OverRide Puzzle #3 for Destiny 2's Vesper's Host
            Dungeon Ice Breaker Catalyst Puzzle
"""


def get_input():
    """checks that the user input is an integer. Continues to prompt
    user until an integer is entered or program is interrupted.

    :return:    (int) target value
    """
    while True:
        try:
            user_in = int(input("Target: "))
            return user_in
        except ValueError:
            print("Error: Invalid input. Target must be an integer")


def access_override_puzzle_2():
    """computes 4 digits (1-9) that can be multiplied together to equal
    target. The 4 digits must be unique.

    :return:    None
    """
    target = get_input()

    # brute force attempt
    # not terrible because only checking 1-9 each loop
    # finds first set of 4 numbers that multiply to target
    for num1 in range(1, 10):
        for num2 in range(1, 10):
            if len({num1, num2}) == 2:
                for num3 in range(1, 10):
                    if len({num1, num2, num3}) == 3:
                        for num4 in range(1, 10):
                            if len({num1, num2, num3, num4}) == 4:
                                if num1 * num2 * num3 * num4 == int(target):
                                    print(f"{num1}, {num2}, {num3}, {num4}")
                                    return

    # optimized attempt?
    # TODO

    print(f"Error: Could not find 4 numbers that multiply to equal {target}")


def access_override_puzzle_3():
    """computes 2 sets of 4 digits such that when the first set is
    added together X and the second set is added together Y, X * Y is
    equal to target. The digits in each set must be unique.

    :return:    None
    """
    target = get_input()

    # brute force attempt


    # optimized attempt

    print(f"Error: Could not find 2 sets of 4 numbers that when added"
          f"make 2 numbers that then multiply to equal {target}")


def main():
    """

    :return:
    """
    access_override_puzzle_2()


if __name__ == "__main__":
    main()
