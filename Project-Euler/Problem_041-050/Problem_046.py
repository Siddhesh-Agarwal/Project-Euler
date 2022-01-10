"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2 × 1^2
    15 = 7 + 2 × 2^2
    21 = 3 + 2 × 3^2
    25 = 7 + 2 × 3^2
    27 = 19 + 2 × 2^2
    33 = 31 + 2 × 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
number = 5
f = 1
primes = set()

while True:
    if all(number % prime for prime in primes):
        primes.add(number)
    else:
        if not any((number-2*i*i) in primes for i in range(1, number)):
            break
    number += 3-f
    f = -f
print(number)