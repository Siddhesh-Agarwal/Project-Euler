"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import sqrt

def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_truncatable_prime(number: int):
    if number < 10:
        return False
    
    # Remove digits from left to right
    number1 = number
    for _ in range(len(str(number))):
        if not is_prime(number1):
            return False
        number1 = number1 // 10 
    
    # Remove digits from right to left
    number2 = number
    for _ in range(len(str(number))):
        if not is_prime(int(number2)):
            return False
        number2 = str(number2)[1:]
    
    return True

count = 0
i = 11
total = 0
while count != 11:
    if is_truncatable_prime(i):
        total += i
        count += 1
        #print(i)
    i += 2
print(total)