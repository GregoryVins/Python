# Определить, какое число в массиве встречается чаще всего

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 3
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

elements_count = []

for i in array:
    count = 0
    for k in array:
        if i == k:
            count += 1
    elements_count.append(count)

i = 0
max_repeat = 0
while i != len(array):
    if elements_count[i] > elements_count[i - 1]:
        max_repeat = elements_count[i]
    i += 1

num_index = elements_count.index(max_repeat)
print(f"Чаще всего встречается число = {array[num_index]}")
