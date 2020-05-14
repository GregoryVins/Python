# https://drive.google.com/file/d/17nydObXht06YFWnlaCmAZKNsub4UnqCJ/view?usp=sharing

"""
Определить, является ли год,
который ввел пользователем,
високосным или не високосным.
"""

year = int(input("Введите год: "))
if year % 400:
    print("Високосный год")
elif year % 4 == 0:
    if year % 100 != 0:
        print("Високосный год")
else:
    print("Обычный год")