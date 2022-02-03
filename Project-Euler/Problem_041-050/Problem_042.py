"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, how many are triangle words?
"""


def word_value(word: str):
    """Returns the value of a word."""
    return sum(ord(letter) - 64 for letter in word)


triangular = lambda x: x * (x + 1) // 2
triangular_numbers = [triangular(i) for i in range(20)]  # more than enough


def is_triangular_number(number: int):
    """Returns True if number is a triangular number."""
    return number in triangular_numbers


with open("./words.txt") as f:
    counter = 0
    words = f.read().split(",")
    for word in words:
        word = word[1:-1]
        value = word_value(word)
        if is_triangular_number(value):
            counter += 1
            # print(word, value)
    print(counter)
