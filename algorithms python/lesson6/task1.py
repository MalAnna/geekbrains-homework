# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.


import random
import sys

def show_size(x):
    print(f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    print(f'Общая память, занятая объектом = {sys.getsizeof(x)}')
    sum_key = 0
    sum_value = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                sum_key = sum_key + sys.getsizeof(key)
                print(f'type = {type(key)}, size = {sys.getsizeof(key)}, object = {key}')
                sum_value = sum_value + sys.getsizeof(value)
                print(f'type = {type(value)}, size = {sys.getsizeof(value)}, object = {value}')
            print(f'Общая память, занятая указателями на переменные = {sum_key}')
            print(f'Общая память, занятая значениями переменных = {sum_value}')
    print(f'Всего занято памяти: {sys.getsizeof(x) + sum_key + sum_value}')

# 2.2.Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_num():
    odd, eve = 0, 0
    num = random.randint(0, 100)

    while num // 10 != 0:
        rem_div = num % 10
        if rem_div % 2 == 0:
            eve = eve + 1
        else:
            odd = odd + 1
        num = num // 10

    rem_div = num % 10

    if rem_div % 2 == 0:
        eve = eve + 1
    else:
        odd = odd + 1

    return vars()

# 3.3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def change_min_max():

    LENG = 10

    lst = [random.randint(0, 100) for i in range(LENG)]
    min_ = lst[0]
    max_ = lst[0]
    pos_min = 0
    pos_max = 0

    for i in range(len(lst)):
        if lst[i] <= min_:
            min_ = lst[i]
            pos_min = i
        elif lst[i] >= max_:
            max_ = lst[i]
            pos_max = i

    lst[pos_max] = min_
    lst[pos_min] = max_

    return vars()

show_size(count_num())
print('*' * 150)
show_size(change_min_max())

# Вывод: указатели на объекты и указатели на переменный в Python занимают примерно в два раза больше памяти,
# чем полезные данные, т.е. значения переменных.
# Расчеты проведены на macOS High Sierra (v. 10.13.6) (x64). Python 3.7.0.
# В первой программе использовалось 4 переменных, во второй программе использовалось 6 переменных и один список,
# при этом первая программа заняла 564 байта памяти, вторая - 1101 байт, что примерно пропорционально количеству
# переменных.

