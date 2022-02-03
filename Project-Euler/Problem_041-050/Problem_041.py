"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from math import sqrt


def is_pandigital(number: int):
    number = str(number)
    return set(number) == set(str(i + 1) for i in range(len(number)))


def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# every 9 digit and 8 digit pandigital number is divisible by 3.
for number in range(10000000, 0, -1):
    if is_pandigital(number) and is_prime(number):
        print(number)
        break
