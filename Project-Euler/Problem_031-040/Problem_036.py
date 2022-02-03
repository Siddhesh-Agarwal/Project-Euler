"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def binary(number):
    return bin(number)[2:]


def is_palindromic(number):
    return str(number) == str(number)[::-1]


total = 0
for i in range(1, 1000000):
    if is_palindromic(i) and is_palindromic(binary(i)):
        # print(i)
        total += i
print(total)
