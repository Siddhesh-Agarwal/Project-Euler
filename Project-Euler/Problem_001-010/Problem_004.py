"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome():
    max_num = 0
    for i in range(1000, 900, -1):
        for j in range(1000, 900, -1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > max_num:
                    max_num = product
    return max_num


print(largest_palindrome())
