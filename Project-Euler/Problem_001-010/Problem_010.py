"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_primes(limit):
    if limit < 2:
        return 0
    total = 2
    for i in range(3, limit, 2):
        if is_prime(i):
            total += i
    return total

print(sum_of_primes(2000000))