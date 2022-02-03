"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def no_of_solutions(perimeter: int):
    """Returns number of unique solutions of possible right angled triamgles for a given perimeter"""
    if perimeter < 3:
        return 0
    solution_count = 0
    for i in range(perimeter // 3):
        for j in range(i, perimeter // 2):
            if i ** 2 + j ** 2 == (perimeter - i - j) ** 2:
                solution_count += 1
    return solution_count


max_i = max([i for i in range(1, 1001)], key=no_of_solutions)

print(max_i)
