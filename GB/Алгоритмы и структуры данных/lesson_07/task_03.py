import random

"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""
M = 6

array = [random.randint(-100, 100) for _ in range(2 * M)]
array.append(random.randint(-100, 100))

half_el = len(array) // 2

result = []

for i in array:
    more = 0
    less = 0
    for j in array:
        if i == j:
            continue
        elif i >= j:
            more += 1
        elif i <= j:
            less += 1
    if more == half_el or less == half_el:
        result.append(i)

print(f'Медианой в данном массиве будет число {set(result)}')

# Проверка
# # array.sort()
# # print(array)
# # print(array[len(array) // 2])
