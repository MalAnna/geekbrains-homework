# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()


from random import choice
from string import ascii_lowercase


def count_subs(s):
    count_hash = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            count_hash.add(hash(s[i:j]))

    if len(s) > 1:
        count = len(count_hash) - 1
    elif len(s) == 1:
        count = 1
    else:
        count = 'Строка должна быть один или больше символов'

    return count


N = int(input('Введите длину строки: '))
s = (''.join(choice(ascii_lowercase) for i in range(N)))
print(f'Сгенерирована строка: {s}')
print(f'В ней найдено {count_subs(s)} уникальных подстрок')


