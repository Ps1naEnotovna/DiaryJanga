# Даны 2 упорядоченных (отсортированных) массива с уникальными элементами,
# найти и вывести их упорядоченное объединение без дубликатов,
# используя константу доп. памяти.

# Input : arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6}
# Output : Union : {1, 2, 3, 4, 5, 6, 7}
import unittest

arr_1 = [1, 2, 3, 4, 5]
# arr_2 = [1, 2, 3, 4, 5]
arr_2 = [6]


def i_dont_know(arr1, arr2):
    result_list = []
    counter_1, counter_2 = 0, 0
    len_arr_1, len_arr_2 = len(arr1) - 1, len(arr2) - 1

    while counter_1 <= len_arr_1 and counter_2 <= len_arr_2:
        if arr1[counter_1] < arr2[counter_2]:
            if not result_list or result_list[-1] != arr1[counter_1]:
                result_list.append(arr1[counter_1])
            counter_1 += 1
        elif arr1[counter_1] > arr2[counter_2]:
            if not result_list or result_list[-1] != arr2[counter_2]:
                result_list.append(arr2[counter_2])
            counter_2 += 1
        else:
            result_list.append(arr1[counter_1])
            counter_1 += 1
            counter_2 += 1

    if counter_1 <= len_arr_1:
        for element in arr1[counter_1:]:
            if result_list[-1] != element:
                result_list.append(element)

    if counter_2 <= len_arr_2:
        for element in arr2[counter_2:]:
            if result_list[-1] != element:
                result_list.append(element)

    return result_list


# print(IDontKnow(arr_1, arr_2))


class AbobaTest(unittest.TestCase):
    def test_ordinary(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], i_dont_know(arr_1, arr_2))

    def test_one_digit(self):
        self.assertEqual([1], i_dont_know([1] * 2, [1]))
        self.assertEqual([1], i_dont_know([1], [1]))

    def test_double_digit(self):
        self.assertEqual([1, 2, 3], i_dont_know([1, 1, 2], [1, 2, 3, 3]))