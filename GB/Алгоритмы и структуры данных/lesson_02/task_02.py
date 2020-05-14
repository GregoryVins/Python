#https://drive.google.com/file/d/1X16iK2XOA7w1tp-jD3Nrf2-nw_RST6wG/view?usp=sharing

"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

user_answer = input("Введите натуральное число: ")
odd, even = 0, 0
for i in user_answer:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"{even=}\n{odd=}")