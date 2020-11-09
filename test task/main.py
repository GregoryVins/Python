# -*- coding: utf-8 -*-

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
