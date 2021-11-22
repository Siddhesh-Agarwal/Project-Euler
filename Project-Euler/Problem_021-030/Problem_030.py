"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_power_of_digits_is_number(number, power):
    total = 0
    for digit in str(number):
        total += pow(int(digit), power)
    return number == total

def sum_of_all_numbers(power):
    total = 0
    for i in range(2, pow(10, power + 1)):
        if sum_of_power_of_digits_is_number(i, power):
            total += i
    return total

print(sum_of_all_numbers(5))