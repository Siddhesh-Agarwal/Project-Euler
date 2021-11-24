"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

total = 0
products = set()
for i in range(1, 10000):
    for j in range(i+1, 10000):
        string = str(i) + str(j) + str(i * j)
        if '0' in string:
            continue
        elif all([len(string) == 9, len(set(string)) == 9, i * j not in products]):
                total += i * j
                products.add(i * j)
        if len(string) > 9:
            break
print(total)