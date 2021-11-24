"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from math import gcd
prod = [1, 1]
for i in range(10, 100):                                            # Loop through all numbers from 10 to 99
    for j in range(i + 1, 100):                                     # i/j < 1 so i < j < 100  
        if i % 10 != 0 and j % 10 != 0:
            common = list(set(str(i)).intersection(set(str(j))))    # Find common digit
            if len(common) == 1:                                    # Check if common digit exists
                common = str(int(common[0]))                        # Convert to string for comparison
                i_new = str(i).replace(common, "")                  # Remove common digit from numerator
                j_new = str(j).replace(common, "")                  # Remove common digit from denominator
                if i_new != "" and j_new != "":                     # Check if numerator and denominator are not empty
                    if int(i_new.strip()) / int(j_new.strip()) == i / j:
                        prod[0] *= i                                # Multiply numerator
                        prod[1] *= j                                # Multiply denominator

print(prod[1] // gcd(prod[0], prod[1]))