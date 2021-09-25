# Даны 2 упорядоченных (отсортированных) массива с уникальными элементами,
# найти и вывести их упорядоченное объединение без дубликатов,
# используя константу доп. памяти.

# Input : arr1[] = {1, 3, 4, 5, 7}
#         arr2[] = {2, 3, 5, 6}
# Output : Union : {1, 2, 3, 4, 5, 6, 7}

arr_1 = [1, 2, 3, 4, 5]
# arr_2 = [1, 2, 3, 4, 5]
arr_2 = [6]

result_list = []
counter_1, counter_2 = 0, 0
len_arr_1, len_arr_2 = len(arr_1) - 1, len(arr_2) - 1

while counter_1 <= len_arr_1 and counter_2 <= len_arr_2:
    if arr_1[counter_1] < arr_2[counter_2]:
        result_list.append(arr_1[counter_1])
        counter_1 += 1
    elif arr_1[counter_1] > arr_2[counter_2]:
        result_list.append(arr_2[counter_2])
        counter_2 += 1
    else:
        result_list.append(arr_1[counter_1])
        counter_1 += 1
        counter_2 += 1

if counter_1 <= len_arr_1:
    result_list += arr_1[counter_1:]

if counter_2 <= len_arr_2:
    result_list += arr_2[counter_2:]