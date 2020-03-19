from sys import getsizeof


# Python 3.8.0 [MSC v.1916 64 bit (AMD64)] on win32
# Программа задействует 1108 байт

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
numerator = [i for i in range(2, 100)]
denominator = [i for i in range(2, 10)]
i = 0
while i != len(denominator):
    k = 0
    count = 0
    while k != len(numerator):
        if numerator[k] % denominator[i] == 0:
            count += 1
        k += 1
    print(f'Числу {numerator[i]} кратно {count} элементов')
    i += 1

print('\nПрограмма задействует', show(numerator, denominator, i, k, count), "байт(а)")
