import unittest


def max_ones(_list: list) -> int:
    """Solution"""
    len_list = len(_list)
    solution = 0
    prima_count = 0
    sec_count = 0
    met_zero = False

    for elem in _list:
        if elem == 1:
            prima_count += 1
            sec_count += 1
            if met_zero:
                met_zero = False
        else:
            met_zero = True
            if prima_count > solution:
                solution = prima_count
            prima_count = sec_count
            sec_count = 0
    if prima_count > solution:
        solution = prima_count
    if solution == len_list or solution == 0:
        solution = len_list - 1
    return solution


print(max_ones([1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(max_ones([1] * 10))


class MaxOnesTest(unittest.TestCase):

    def test_only_ones(self):
        self.assertEqual(9, max_ones([1] * 10))

    def test_single_zero(self):
        self.assertEqual(6, max_ones([1, 1, 1, 1, 0, 1, 1]))
        self.assertEqual(6, max_ones([1, 1, 1, 1, 0, 1, 1, 0, 1]))
        self.assertEqual(9, max_ones([1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]))
