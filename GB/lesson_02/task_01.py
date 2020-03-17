# https://drive.google.com/file/d/1X16iK2XOA7w1tp-jD3Nrf2-nw_RST6wG/view?usp=sharing

"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна
сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности
деления на ноль, если он ввел его в качестве делителя.
"""
print("Введите два натуральных числа и знак операции")
while True:
    num_1 = int(input("Первое число: "))
    num_2 = int(input("Второе число: "))
    symbol = input("Символ операции: ")
    if symbol == "0":
        print("See you soon")
        break
    elif symbol == "+":
        print(num_1 + num_2)
    elif symbol == "-":
        print(num_1 - num_2)
    elif symbol == "*":
        print(num_1 * num_2)
    elif symbol == "/":
        if num_2 == 0:
            print("Нельзя делить на ноль")
        else:
            print(num_1 / num_2)
    else:
        print("Что-то пошло не так, повторите ввод...")