"""Дается матрица n*m, в рядах которой все элементы возрастают,
а последний элемент ряда гаранированно меньше первого элемента следующего ряда

Дано число, задача - определить его коорднинаты в матрице или выдать False в случае отсутствия"""

import unittest
from typing import Union

example = [[1, 2, 3],
           [4, 6, 9],
           [10, 12, 16],
           [20, 21, 49]]


def find_elem(matrix: list[list[int, ...]],
              item: int) -> Union[tuple[int, int], bool]:
    matrix_low, matrix_high = 0, len(matrix) - 1
    while matrix_low <= matrix_high:
        row = (matrix_low + matrix_high) // 2
        if matrix[row][-1] == item:
            return row, -1
        elif item < matrix[row][-1]:
            if item == matrix[row][0]:
                return row, 0
            if item > matrix[row][0]:
                result_row = matrix[row]
                low, high = 0, len(result_row) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if result_row[mid] == item:
                        return row, mid
                    elif item < result_row[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                return False
            else:
                matrix_high = row - 1
        else:
            matrix_low = row + 1
    return False


# print(find_elem(example, 9))


class FindElemTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual((1, -1), find_elem(example, 9))
        self.assertEqual((3, 1), find_elem(example, 21))
        self.assertEqual((1, 0), find_elem(example, 4))

    def test_false(self):
        self.assertFalse(find_elem(example, 24))
        self.assertFalse(find_elem(example, 5))
        self.assertFalse(find_elem(example, 7))