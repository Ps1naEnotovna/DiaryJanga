import unittest


def validate(_list: list) -> None:
    not_right = [a for a in _list if a not in (0, 1)]
    if not_right:
        raise ValueError


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
    if solution == len_list:
        solution = len_list - 1
    return solution


class MaxOnesTest(unittest.TestCase):
    """Tests for max_ones function"""
    def test_only_ones(self):
        self.assertEqual(9, max_ones([1] * 10))

    def test_only_zeros(self):
        self.assertEqual(0, max_ones([0] * 10))

    def test_pogranichnikov(self):
        self.assertEqual(1, max_ones([1, 0]))
        self.assertEqual(1, max_ones([0, 1]))

    def test_single_zero(self):
        self.assertEqual(6, max_ones([1, 1, 1, 1, 0, 1, 1]))
        self.assertEqual(6, max_ones([1, 1, 1, 1, 0, 1, 1, 0, 1]))
        self.assertEqual(9, max_ones([1, 1, 1, 1, 0, 1, 1, 1,
                                      0, 1, 1, 1, 1, 1, 1]))

    def test_many_zero(self):
        self.assertEqual(6, max_ones([1, 0, 0, 0, 1, 1, 1, 1, 1, 1]))
        self.assertEqual(5, max_ones([1, 1, 1, 1, 1, 0, 0, 1, 1]))
        self.assertEqual(7, max_ones([1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
                                      1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]))

    def test_validate(self):
        with self.assertRaises(ValueError):
            validate([1, 0, 0, 1, 2, 1, 0])
