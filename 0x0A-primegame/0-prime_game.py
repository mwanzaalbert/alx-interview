#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Prime Game
"""
__author__ = "Albert Mwanza"
__license__ = "MIT"
__date__ = "2024-12-09"
__version__ = "1.0"


def isWinner(x, nums):
    """
    Determine the winner of the prime number game.

    Args:
        x (int): Number of rounds.
        nums (list of int): List of integers, where each integer represents
                            n for that round.

    Returns:
        str: Name of the player that won the most rounds ('Maria' or 'Ben').
             Return None if there's a tie.
    """
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(max_n):
        """
        Generate a list of primes up to max_n using the Sieve of Eratosthenes.

        Args:
            max_n (int): The upper limit to generate primes.

        Returns:
            list: A list where prime[i] is True if i is prime, False otherwise.
        """
        prime = [True] * (max_n + 1)
        prime[0] = prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(max_n**0.5) + 1):
            if prime[i]:
                for multiple in range(i * i, max_n + 1, i):
                    prime[multiple] = False
        return prime

    max_n = max(nums)
    prime = sieve_of_eratosthenes(max_n)

    def count_primes_up_to(n):
        """
        Count the number of primes up to n.

        Args:
            n (int): The upper limit.

        Returns:
            int: The count of primes up to n.
        """
        return sum(prime[:n + 1])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n)
        if prime_count % 2 == 1:  # Maria wins if the count of primes is odd
            maria_wins += 1
        else:  # Ben wins if the count of primes is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
