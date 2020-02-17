# https://drive.google.com/file/d/17nydObXht06YFWnlaCmAZKNsub4UnqCJ/view?usp=sharing
"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

aph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v,''w', 'x',
       'y', 'z']
user_answer = int(input("Введите номер буквы в латинском алфавите: "))

print(aph[user_answer - 1])
