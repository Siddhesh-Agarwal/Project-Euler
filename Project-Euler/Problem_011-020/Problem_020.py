"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def sum_of_digits(number):
    number = str(number)
    total = 0
    for digit in number:
        total += int(digit)
    return total


def main():
    factorial = 1
    for i in range(1, 101):
        factorial *= i
        if factorial % 10 == 0:
            factorial //= 10
    return sum_of_digits(factorial)


print(main())
