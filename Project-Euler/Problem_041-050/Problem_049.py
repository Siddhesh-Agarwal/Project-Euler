"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from math import sqrt
from itertools import permutations

# create a list of 4 digits primes
primes_arr = []
for number in range(1000, 10000):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            break
    else:
        primes_arr.append(number)

# function to return the permutations an integer
def permute(n: int):
    return [int(''.join(i)) for i in permutations(str(n))]

# prime permuations
def prime_permutations(n: int):
    perms = permute(n)
    prime_perms =[]
    for p in perms:
        if p in primes_arr:
            prime_perms.append(p)
    prime_perms.remove(n)
    return sorted(prime_perms)

# find the sequence
def sequence(n: int):
    seq_bool=False
    global seq
    seq=[]
    fin =[]
    perms = prime_permutations(n)
    for q in perms:
        if (q+(q-n)) in perms:
            seq =[n,q,2*q-n]
            seq_bool=True
    return seq_bool

for prime in primes_arr:
    if sequence(prime):
        if seq != [seq[0]]*3:
            print(seq)