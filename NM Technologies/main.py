# -*- coding: utf-8 -*-

# Имеем dictionary со следующей структурой и данными:
# d = {
#     "a": 5,
#     "b": 6,
#     "c": {
#         "f": 9,
#         "g": {
#             "m": 17,
#             "n": 3
#         }
#     }
# }

# Необходимо написать функцию flatten(d), которая на входе получает dictionary с указанной выше структурой и возвращает dictionary вида:
#     {
#         'a': 5,
#         'b': 6,
#         'c.f': 9,
#         'c.g.m': 17,
#         'c.g.n': 3
#     }
# Алгоритм должен работать для общего случая, т.е. превращать любой многоуровневый dictionary в одноуровневый, с ключами, как указано выше.

def flatten(d: dict):
    """
    Рекурсивно итерируется по многоуровневому словарю и возвращает одноуровневый словарь,
    отображая вложенность через точку.
    :param d: Словарь.
    :return: Одноуровневый словарь.
    """
    result = dict()
    for k, v in d.items():
        if type(v) != dict:
            result[k] = v
        else:
            spam = flatten(v)
            for key, value in spam.items():
                result[f'{k}.{key}'] = value

    return result
