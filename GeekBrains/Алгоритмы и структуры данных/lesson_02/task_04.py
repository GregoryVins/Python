# https://drive.google.com/file/d/1X16iK2XOA7w1tp-jD3Nrf2-nw_RST6wG/view?usp=sharing

def foo(x):
    """
     Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
     Количество элементов (n) вводится с клавиатуры.
    """
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return (foo(x - 1) / 2) + (foo(x - 2) / 2)

user_answer = int(input("Введите натуральное число: "))
print(foo(user_answer))
