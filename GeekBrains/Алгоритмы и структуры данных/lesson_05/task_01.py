from collections import namedtuple

"""
Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

"""

N = int(input('Введите количество предприятий (Натуральное число): '))
Company = namedtuple('Company', 'name, profit')
result = []
total = 0

if N != 0:
    for comp in range(N):
        name = input(f'Введите название предприятия №{comp + 1}: ')
        profit = 0
        for i in range(4):
            profit += int(input(f'Введите прибыль компании за {i + 1} четверть: '))
        result.append(Company(name, profit))
        total += profit

    middle_profit = total / N
    print(f'\nСредняя прибыль = {middle_profit}\n')

    # Идея части с выводом позаимствована с разбора ДЗ, ранее вывод осуществлялся в одном цикле с двумя ветвлениями
    for company in result:
        if company[1] > middle_profit:
            print(f'Компания {company[0]} имеет прибыль выше среднего, которая равна {company[1]}')

    print('\n')

    for company in result:
        if company[1] < middle_profit:
            print(f'Компания {company[0]} имеет прибыль ниже среднего, которая равна {company[1]}')
else:
    print(None)
