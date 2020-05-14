# https://drive.google.com/file/d/17nydObXht06YFWnlaCmAZKNsub4UnqCJ/view?usp=sharing
"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""

a = int(input("Введите три разных числа.\nПервое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a > b > c or a < b < c:
    print(b)
elif a > c > b or b < c < a:
    print(c)
else:
    print(a)
