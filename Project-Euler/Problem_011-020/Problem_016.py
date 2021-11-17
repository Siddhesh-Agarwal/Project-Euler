"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
from math import pow

def sum_of_digits(number):
    number = str(int(number))
    total = 0
    for digit in number:
        total += int(digit)
    return total

print(sum_of_digits(pow(2, 1000)))