"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def sum_of_diagonal_in_spiral(side):
    diagonal1 = 0
    element = 1
    diagonal2 = 0
    for i in range(1, side + 1):
        diagonal1 += element
        if i != 1 and i % 2 == 1:
            diagonal2 += 2 * element
        element += 2 * i

    return diagonal1 + diagonal2


print(sum_of_diagonal_in_spiral(1001))
