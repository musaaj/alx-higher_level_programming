#!/usr/bin/python3
"""
generate pascal triangle
"""


def pascal_triangle(n):
    """generate pascal triangle from aa given input

    Args:
        n: int

    Return: 2d matrix of pascal triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    for i in range(n - 1):
        last_row = triangle[i]
        last_row_len = len(last_row)
        new_row = [1]
        j = 0
        while j < last_row_len - 1:
            new_row.append(last_row[j] + last_row[j + 1])
            j += 1
        new_row.append(1)
        triangle.append(new_row)
    return triangle
