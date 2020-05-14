import hashlib


def substr_in_srt(n):
    """
    Функция возвращает количество подстрок в строке n
    """
    if len(n) == 0 or len(n) == 1:
        return len(n)
    result = set()
    count = 1
    while count < len(n):
        for i in range(len(n)):
            result.add(hashlib.sha1(n[i:i + count].encode('utf-8')).hexdigest())
        count += 1
    return len(result)


user_answer = input('Введите строку: ')
print(f'Количество подстрок: {substr_in_srt(user_answer)}')
