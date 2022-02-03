"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def number_to_words(number):
    """Converts a number to words."""
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    hundreds = [
        "",
        "one hundred",
        "two hundred",
        "three hundred",
        "four hundred",
        "five hundred",
        "six hundred",
        "seven hundred",
        "eight hundred",
        "nine hundred",
    ]
    if number == 1000:
        return "one thousand"
    elif number >= 100:
        beyond = number % 100
        seperator = " and " if beyond > 0 else " "
        return hundreds[number // 100] + seperator + number_to_words(number % 100)
    elif number >= 20:
        return tens[number // 10] + " " + units[number % 10]
    elif number >= 10:
        return [
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ][number - 10]
    else:
        return units[number]


def char_count(words):
    """Returns the number of characters in a number."""
    length = 0
    for char in words:
        if char.isalpha():
            length += 1
    return length


print(sum(char_count(number_to_words(i)) for i in range(1, 1001)))
