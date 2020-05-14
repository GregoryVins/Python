import random

"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


def merge_sort(arr):
    """Сортировка методом слияния"""
    result = []

    if len(arr) < 2:
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    result += left
    result += right
    return result


array = [round(random.random() * 49.9, 1) for _ in range(10)]
random.shuffle(array)
print('Неотсортированный массив: \n', array)
print('Oтсортированный массив: \n', merge_sort(array))

assert merge_sort(array) == sorted(array)
