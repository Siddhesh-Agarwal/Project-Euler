"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial

fetch_factorial = {x: factorial(x) for x in range(10)}
total = 0

for i in range(10, 1000000):
    if sum(fetch_factorial[int(x)] for x in str(i)) == i:
        # print(i)
        total += i
print(total)
