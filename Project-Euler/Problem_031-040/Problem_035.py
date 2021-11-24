"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from math import sqrt

def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, round(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_circular_prime(number: int):
    for _ in range(len(str(number))):
        if not is_prime(int(number)):
            return False
        number = str(number)[1:] + str(number)[0]
    return True


count = 0
for number in range(1000000):
    if is_circular_prime(number):
        #print(number)
        count += 1
print(count)
