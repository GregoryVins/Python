# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = -800
MAX_ITEM = -750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num, min_num = 0, 0
for i in range(len(array)):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i

array[min_num], array[max_num] = array[max_num], array[min_num]
print(array)
