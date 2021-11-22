"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def main(x):
    numbers = set()

    for num in range(1, x):
        x_val = 0
        y_val = 0

        for val in range(1, num):
            if (num % val) == 0:
                x_val += val

        for val in range(1, x_val):
            if (x_val % val) == 0:
                y_val += val

        if y_val == num and x_val != y_val:
            numbers.add(y_val)

    return sum(numbers)

print(main(10000))