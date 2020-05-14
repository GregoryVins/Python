# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num, min_num = 0, 0
for i in range(len(array)):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i

new_array = array[min_num + 1:max_num] or array[max_num + 1:min_num]
print(new_array)
array_sum = 0
for i in new_array:
    array_sum += i

assert array_sum == sum(new_array)

