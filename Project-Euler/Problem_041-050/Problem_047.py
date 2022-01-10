"""
The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
"""

def prime_factors(number: int):
    """Returns the list of prime factors of the given number."""
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 2 if divisor > 2 else 1
    return factors

counter = 0
number = 1
while counter < 4:
    if len(set(prime_factors(number))) == 4:
        counter += 1
    else:
        counter = 0
    number += 1
print(number - 4)