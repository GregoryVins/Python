# https://drive.google.com/file/d/17nydObXht06YFWnlaCmAZKNsub4UnqCJ/view?usp=sharing

"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""
number = int(input("Введите целое трёхзначное число: "))
num_1 = number // 100
num_3 = number % 10
num_2 = number // 10
num_2 = num_2 % 10
summ = num_1 + num_2 + num_3
multiplicate = num_1 * num_2 * num_3
print(f"{summ=}, {multiplicate=}")