from sys import getsizeof


# Python 3.8.0 [MSC v.1916 64 bit (AMD64)] on win32
# Программа задействует 84 байта

def show(*args):
    summ = 0
    for i in args:
        print(f'type={type(i)}, size={getsizeof(i)}, {i=}')
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    show(key)
                    show(value)
            elif not isinstance(i, str):
                for item in i:
                    show(item)
        summ += getsizeof(i)
    return summ


# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
for i in range(2, 10):
    count = 0
    for k in range(2, 100):
        if k % i == 0:
            count += 1
    print(f'Числу {i} кратно {count} элементов')

print('\nПрограмма задействует', show(i, count, k), "байт(а)")


"""
ВЫВОД:
Очевидно, что вариант №1 является лучшим из всех представленных, т.к. не забирает память на создание словаря
(вариант №2) или массивов (варинат №3). Итерация происходит в сгенерированном ряду чисел в рамках заданного диапазона,
а так же используются всего три переменные
"""