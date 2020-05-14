# https://drive.google.com/file/d/17nydObXht06YFWnlaCmAZKNsub4UnqCJ/view?usp=sharing
"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

aph = 'abcdefghijklmnopqrtuvwxyz'
user_answer = int(input("Введите номер буквы в латинском алфавите: "))

print(aph[user_answer - 1])
