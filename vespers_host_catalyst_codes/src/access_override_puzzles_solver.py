"""
File:       access_override_puzzles_solver.py
Author:     Garret Wilson
Purpose:    provides possible inputs to Access Override Puzzle #2 and
            Access OverRide Puzzle #3 for Destiny 2's Vesper's Host
            Dungeon Ice Breaker Catalyst Puzzle
"""


def get_input():
    """Checks that the user input is an integer. Continues to prompt
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
    """Computes 4 digits (1-9) that can be multiplied together to equal
    target. The 4 digits must be unique.

    :return:    None
    """
    target = get_input()

    # limits number of combinations checked
    for num1 in range(1, 7):
        for num2 in range(num1+1, 8):
            for num3 in range(num2+1,  9):
                for num4 in range(num3+1, 10):
                    if num1 * num2 * num3 * num4 == target:
                        print("-----------------------")
                        print(f"Set: {num1}, {num2}, {num3}, {num4}")
                        return

    print(f"Error: Could not find 4 unique numbers that multiply to equal "
          f"{target}")


def sum_four_digits(target):
    """Determines if target can be the sum of four unique digits (1-9)

    :param target:  (int) target value
    :return:        (str) string of four unique digits if possible, empty
                    string otherwise
    """
    for a in range(1, 7):
        for b in range(a+1, 8):
            for c in range(b+1, 9):
                for d in range(c+1, 10):
                    if a + b + c + d == target:
                        return f"{a}, {b}, {c}, {d}"

    return ""


def access_override_puzzle_3():
    """Computes 2 sets of 4 digits such that when the first set is
    added together X and the second set is added together Y, X * Y is
    equal to target. The digits in each set must be unique.

    :return:    None
    """
    target = get_input()

    # brute force attempt
    # start by getting all of targets divisors
    # map divisors to key:value pairs in dict
    pairs = {}

    for div1 in range(1, target+1):
        if (
            target % div1 == 0 &
            div1 not in pairs.keys() and
            div1 not in pairs.values()
        ):
            div2 = target / div1
            pairs[div1] = div2

    # loop over key:value pairs until find one where key and value can be
    #   made up of 4 distinct numbers
    for k, v in pairs.items():
        set1 = sum_four_digits(k)
        set2 = sum_four_digits(v)

        if set1 != "" and set2 != "":
            print("-----------------------")
            print(f"First set: {set1}")
            print(f"Second set: {set2}")
            return

    print(f"Error: Could not find 2 sets of 4 unique numbers that when added"
          f" make 2 numbers that then multiply to equal {target}")


def main():
    """Prompts the user to choose the access override puzzle 2 solver
    or the access override 3 puzzle solver. Continues to prompt user
    until a valid input is provided or program is interrupted.

    :return:    None
    """
    user_in = input("Access override puzzle 2 solver (p2) or access "
                    "override puzzle 3 solver (p3)? ")

    while True:
        if user_in.lower() == "p2":
            access_override_puzzle_2()
            exit(code=0)

        if user_in.lower() == "p3":
            access_override_puzzle_3()
            exit(code=0)

        else:
            print("Error: must enter 'p2' for puzzle 2 or 'p3' for puzzle 3")
            user_in = input()


if __name__ == "__main__":
    main()
