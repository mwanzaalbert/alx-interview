#!/usr/bin/python3
"""
The module contains a function `minOperations` that calculates the
minimum number of operations required to get exactly `n` H characters
in a text file using only two operations: 'Copy All' and 'Paste'.

The function is optimized using prime factorization to minimize the
number of operations needed.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n H characters in the text file.

    Operations allowed:
    - Copy All
    - Paste

    Parameters:
    n (int): The target number of H characters to reach.

    Returns:
    int: The minimum number of operations required to get exactly `n`
    H characters. If `n` is impossible to achieve (e.g., n <= 1), return 0.

    Example:
    >>> minOperations(9)
    6
    >>> minOperations(4)
    4
    >>> minOperations(12)
    7
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n,
                                                            minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n,
                                                            minOperations(n)))
