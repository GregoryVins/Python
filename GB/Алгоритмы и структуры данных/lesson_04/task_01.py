import timeit
import cProfile


# 1) Рекурсия
def foo_1(x):
    """
     Находит сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    """
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return (foo_1(x - 1) / 2) + (foo_1(x - 2) / 2)

print('===== #1 FUNCTION =====\n')
print(timeit.timeit('foo_1(5)', number=100, globals=globals()))  # 0.00041200000000000264
print(timeit.timeit('foo_1(10)', number=100, globals=globals()))  # 0.005245800000000002
print(timeit.timeit('foo_1(15)', number=100, globals=globals()))  # 0.0562299
print(timeit.timeit('foo_1(20)', number=100, globals=globals()))  # 0.7433042
print(timeit.timeit('foo_1(25)', number=100, globals=globals()))  # 7.108796
cProfile.run('foo_1(5)')  # 15/1    0.000    0.000    0.000    0.000 task_01.py:5(foo_1)
cProfile.run('foo_1(10)')  # 177/1    0.000    0.000    0.000    0.000 task_01.py:5(foo_1)
cProfile.run('foo_1(20)')  # 21891/1    0.019    0.000    0.019    0.019 task_01.py:6(foo_1)
cProfile.run('foo_1(30)')  # 2692537/1    1.985    0.000    1.985    1.985 task_01.py:6(foo_1)


# 2) Второй способ
def foo_2(n):
    numbers = [1]
    summ = 1
    for _ in range(n + 1):
        numbers.append(numbers[-1] / -2)
        summ += numbers[-1]
    return summ


print('===== #2 FUNCTION =====\n')
print(timeit.timeit('foo_2(500)', number=100, globals=globals()))  # 0.017479800000000267
print(timeit.timeit('foo_2(1000)', number=100, globals=globals()))  # 0.0384525
print(timeit.timeit('foo_2(2000)', number=100, globals=globals()))  # 0.0708151000000008
print(timeit.timeit('foo_2(4000)', number=100, globals=globals()))  # 0.15272240000000004
print(timeit.timeit('foo_2(8000)', number=100, globals=globals()))  # 0.29274179999999994
cProfile.run('foo_2(10)')  # 11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('foo_2(20)')  # 21    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('foo_2(40)')  # 41    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


# 3) Рекурсия + Мемоизация
def foo_3(n):
    summ = {
        1: 1,
        2: 0.5,
    }

    def _numb(n):
        if n in summ:
            return summ[n]
        summ[n] = (_numb(n - 1) / 2) + (_numb(n - 2) /2)
        return summ[n]
    return _numb(n)


print('===== #3 FUNCTION =====\n')
print(timeit.timeit('foo_3(50)', number=100, globals=globals()))  # 0.005360799999999999
print(timeit.timeit('foo_3(100)', number=100, globals=globals()))  # 0.011014000000000003
print(timeit.timeit('foo_3(200)', number=100, globals=globals()))  # 0.030840399999999997
print(timeit.timeit('foo_3(400)', number=100, globals=globals()))  # 0.0450064
print(timeit.timeit('foo_3(800)', number=100, globals=globals()))  # 0.1097911
cProfile.run('foo_3(200)')  # 397/1    0.001    0.000    0.001    0.001 task_01.py:57(_numb)
cProfile.run('foo_3(400)')  # 797/1    0.001    0.000    0.001    0.001 task_01.py:57(_numb)
cProfile.run('foo_3(800)')  # 1597/1    0.002    0.000    0.002    0.002 task_01.py:57(_numb)


"""
ВЫВОД: 
    На мой взгляд, самым оптимальным будет являться вариант №2, т.к. он беспрецедентный лидер по скорости обработки.
    
Вариант №1 имеет логарифимическую зависимость и скорость измерения чисел 30+ и выше занимает довольно
длительный период времени, рекурсивный поиск результата считаю самым худшим по затратам времени и кол-ву вызова функции.

Вариант №2 имеет линейную зависимость и скорость измерения растёт пропорционально искомому элементу. Минусом является
затрата времени на добавление нового элемента в список, а так же использование памяти для хранения ссылок на объект 
numbers при большом объеме информации или большого запрашиваемого числа суммы конкретного ряда чисел.

Вариант №3 рекурсия + мемоизация, работает значительно быстрее варианта №1, за счёт словаря и сохранения данных,
функции не приходится вызывать саму себя большое кол-во раз. Линейная зависимость
"""