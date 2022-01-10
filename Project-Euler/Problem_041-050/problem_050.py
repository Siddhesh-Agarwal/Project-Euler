"""
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from math import sqrt

def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes"""
    prime_list = [True] * (n + 1)
    prime_list[0] = prime_list[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if prime_list[i]:
            for j in range(i * i, n + 1, i):
                prime_list[j] = False
    return [i for i in range(len(prime_list)) if prime_list[i]]

sieve = sieve_of_eratosthenes(1000000)
length = 0
largest = 0
last = len(sieve)
for i in range(len(sieve)):
    for j in range(i + length, last):
        sum_of_sublist = sum(sieve[i:j])
        if sum_of_sublist < 1000000:
            if sum_of_sublist in sieve:
                length = j - i
                largest = sum_of_sublist
        else:
            last = j + 1
            break
print(largest)