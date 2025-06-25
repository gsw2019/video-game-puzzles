"""
File:           access_override_puzzles_solver.py
Author:         Garret Wilson
Date:           06/24/25
Description:    Contains the logic used to solve each puzzle
"""


def puzzle_2(target):
    """Computes 4 digits (1-9) that can be multiplied together to equal
    target. The 4 digits must be unique.

    :param target:  (int) target value
    :return:        (str) string of four unique digits if found, empty
                    string otherwise
    """

    # limits number of combinations checked
    for a in range(1, 7):
        for b in range(a+1, 8):
            for c in range(b+1,  9):
                for d in range(c+1, 10):
                    if a * b * c * d == target:
                        return f"Set: {a}, {b}, {c}, {d}"

    return ""


def find_unique_sum_set(target):
    """Determines if target can be the sum of four unique digits (1-9)

    :param target:  (int) target value
    :return:        (str) string of four unique digits if found, empty
                    string otherwise
    """
    for a in range(1, 7):
        for b in range(a+1, 8):
            for c in range(b+1, 9):
                for d in range(c+1, 10):
                    if a + b + c + d == target:
                        return f"{a}, {b}, {c}, {d}"

    return ""


def puzzle_3(target):
    """Computes 2 sets of 4 digits such that when the first set is
    added together X and the second set is added together Y, X * Y is
    equal to target. The digits in each set must be unique.

    :param target:  (int) target value
    :return:        (str) string of two sets of four digits if found,
                    empty string otherwise
    """

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
        set1 = find_unique_sum_set(k)
        set2 = find_unique_sum_set(v)

        if set1 != "" and set2 != "":
            return (f"First set: {set1}"
                    f"Second set: {set2}")
        else:
            return ""
