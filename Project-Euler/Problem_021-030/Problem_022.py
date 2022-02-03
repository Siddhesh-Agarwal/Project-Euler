"""
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def alphabetical_value(name):
    """Returns the alphabetical value of a name."""
    return sum(ord(c) - 64 for c in name)


with open("./names.txt", "r+") as f:
    names = f.read().split(",")
    names.sort()
    total = 0
    for pos, name in enumerate(names):
        total += alphabetical_value(name[1:-1]) * (pos + 1)
    print(total)
