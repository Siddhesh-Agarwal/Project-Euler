"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	 = 	0.5
    1/3	 = 	0.(3)
    1/4	 = 	0.25
    1/5	 = 	0.2
    1/6	 = 	0.1(6)
    1/7	 = 	0.(142857)
    1/8	 = 	0.125
    1/9  = 	0.(1)
    1/10 = 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def longest_recurring_cycle(limit):
    """Find the longest recurring cycle in the decimal fraction part of 1/d."""
    max_len = 0
    max_d = 1

    for d in range(1, limit):
        quotient = {0: 0}
        curr_value = 1
        len_recr = 0

        while curr_value not in quotient:
            len_recr += 1
            quotient[curr_value] = len_recr
            curr_value = (curr_value % d) * 10

        if not curr_value:
            continue

        len_recr -= quotient[curr_value]

        if len_recr > max_len:
            max_len = len_recr
            max_d = d

    return max_d


print(longest_recurring_cycle(1000))
