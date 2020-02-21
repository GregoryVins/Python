import random

# https://drive.google.com/file/d/1X16iK2XOA7w1tp-jD3Nrf2-nw_RST6wG/view?usp=sharing

"""
В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться, больше или 
меньше введенное пользователем число, чем то, что загадано. 
Если за 10 попыток число не отгадано, вывести правильный ответ.
"""

print("Отгадайте натуральное число от 0 до 100")
answer = random.randint(0, 100)
count = 10
while count != 0:
    user_answer = int(input("Ваш ответ: "))
    if user_answer == answer:
        print("Вы выйграли! Правильный ответ", answer)
        break
    elif user_answer > answer:
        count -= 1
        print(f"Неверно, мы ищем число меньше. Попыток осталось: {count}")
    elif user_answer < answer:
        count -= 1
        print(f"Неверно, мы ищем число больше. Попыток осталось: {count}")
else:
    print("Вы проиграли, оппытки закончились. Правильный ответ:", answer)