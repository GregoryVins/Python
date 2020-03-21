from sys import getsizeof


# Python 3.8.0 [MSC v.1916 64 bit (AMD64)] on win32
# Программа задействует 472 байта

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
res = {i: 0 for i in range(2, 10)}
for i in res:
    for k in range(2, 100):
        if k % i == 0:
            res[i] += 1

for key, value in res.items():
    print(f'Числу {key} кратно {value} элементов')

print('\nПрограмма задействует', show(res, i, k, key, value), "байт(а)")
