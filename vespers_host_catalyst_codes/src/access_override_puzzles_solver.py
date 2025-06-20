"""
File:       access_override_puzzles_solver.py
Author:     Garret Wilson
Purpose:    provides possible inputs to Access Override Puzzle #2 and
            Access OverRide Puzzle #3 for Destiny 2's Vesper's Host
            Dungeon Ice Breaker Catalyst Puzzle
"""


def input_is_valid(target):
    """checks that the user input is an integer

    :param target:  (str) user input
    :return:        None
    """
    if not target.isnumeric():
        print("Error: Invalid input. Must be an integer")
        exit(code=1)


def access_override_puzzle_2(target):
    """computes 4 digits (1-9) that can be multiplied together to equal
    target. The 4 digits must be unique.

    :param target:  (str) target value
    :return:        None
    """
    input_is_valid(target)

    # brute force attempt
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


def access_override_puzzle_3(target):
    """computes 2 sets of 4 digits such that when the first set is
    added together X and the second set is added together Y, X * Y is
    equal to target. The digits in each set must be unique.

    :param target:  (str) target value
    :return:        (str) 2 sets of 4 digits numbers
    """
    input_is_valid(target)

    # brute force attempt


    print(f"Error: Could not find 2 sets of 4 numbers that when added"
          f"make 2 numbers that then multiply to equal {target}")


def main():
    """

    :return:
    """
    user_in = input("Target: ")
    access_override_puzzle_2(user_in)


if __name__ == "__main__":
    main()
