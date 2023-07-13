#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result in exactly n H
characters in the file
"""


def minOperations(n):
    """ return the number of minimum operations required """
    num_chars_file = 1
    num_chars_clipboard = 0
    num_operations = 0

    while num_chars_file < n:
        if num_chars_clipboard == 0:
            num_chars_clipboard = num_chars_file
            num_operations += 1

        if num_chars_file == 1:
            num_chars_file += num_chars_clipboard
            num_operations += 1
            continue

        remaining_chars_paste = n - num_chars_file

        if remaining_chars_paste < num_chars_clipboard:
            return 0

        if remaining_chars_paste % num_chars_file != 0:
            num_chars_file += num_chars_clipboard
            num_operations += 1
        else:
            num_chars_clipboard = num_chars_file
            num_chars_file += num_chars_clipboard
            num_operations += 2

    if num_chars_file == n:
        return num_operations
    else:
        return 0
