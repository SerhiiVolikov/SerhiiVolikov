from math import pi
from typing import Any

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
other_matrix = [[9, 8, 7], [6, 5, 4], [1, 1, 1]]

text = 'This is a text sample'
print(text)


def get_determinat(the_matrix):
    main_d = 1
    secondary_d = 1
    for row in range(len(the_matrix)):
        for column in range(len(the_matrix[0])):
            if row == column:
                main_d *= the_matrix[row][column]
            if row + column == len(the_matrix) - 1:
                secondary_d *= the_matrix[row][column]
    determinant = main_d - secondary_d
    return determinant


def circle(r=1):
    S = pi * r ** 2
    return S


def sum_numbers(b, a=1, c=0, d=0, e=0, f=0):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    return a + b + c + d + e + f


if __name__ == "__main__":
    print(circle())
    print(circle(69))
    print(sum_numbers(69, 1))
