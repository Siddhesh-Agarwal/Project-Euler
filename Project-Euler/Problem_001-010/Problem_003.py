"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(num):
    max_prime = None
    for i in range(2, int(sqrt(num)) + 1):
        if is_prime(i):
            if 600851475143 % i == 0:
                max_prime = i
    return max_prime


print(largest_prime_factor(600851475143))
