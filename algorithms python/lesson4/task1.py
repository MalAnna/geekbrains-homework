# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

# 1. Вариант
import random
import timeit
import cProfile


def sum_min_max1(l):

    lst = [random.randint(0, l * l) for i in range(l)]
    min_ = lst[0]
    max_ = lst[0]
    pos_min = 0
    pos_max = 0
    summ_ = 0

    for i in range(len(lst)):
        if lst[i] <= min_:
           min_ = lst[i]
           pos_min = i
        elif lst[i] >= max_:
           max_ = lst[i]
           pos_max = i

    if pos_min < pos_max and pos_max - pos_min != 1:
        if pos_min + 1 == pos_max - 1:
            summ_ = lst[pos_min + 1]
        else:
            for i in range((pos_min + 1), pos_max):
                summ_ = summ_ + lst[i]

    elif pos_min > pos_max and pos_min - pos_max != 1:
        if pos_min - 1 == pos_max + 1:
            summ_ = lst[pos_max + 1]
        else:
            for i in range((pos_max + 1), pos_min):
                summ_ = summ_ + lst[i]


# "task1.sum_min_max1(10)" 100 loops, best of 5: 13.9 usec per loop
# "task1.sum_min_max1(100)" 100 loops, best of 5: 143 usec per loop
# "task1.sum_min_max1(1000)" 100 loops, best of 5: 1.29 msec per loop
# "task1.sum_min_max1(10000)" 100 loops, best of 5: 13.5 msec per loop
#  cProfile.run('sum_min_max1(10)') 1    0.000    0.000    0.000    0.000 task1.py:10(sum_min_max1)
#  cProfile.run('sum_min_max1(100)') 1    0.000    0.000    0.001    0.001 task1.py:10(sum_min_max1)
#  cProfile.run('sum_min_max1(1000)') 1    0.000    0.000    0.002    0.002 task1.py:10(sum_min_max1)
#  cProfile.run('sum_min_max1(10000)') 1    0.001    0.001    0.022    0.022 task1.py:10(sum_min_max1)

# 2. Вариант

def sum_min_max2(l):

    lst = [random.randint(0, l * l) for i in range(l)]

    min_ = lst.index(min(lst))
    max_ = lst.index(max(lst))

    if min_ > max_:
        min_, max_ = max_, min_
    sum_ = sum(lst[(min_ + 1): max_])

# "task1.sum_min_max2(10)" 100 loops, best of 5: 13.4 usec per loop
# "task1.sum_min_max2(100)" 100 loops, best of 5: 133 usec per loop
# "task1.sum_min_max2(1000)" 100 loops, best of 5: 1.22 msec per loop
# "task1.sum_min_max2(10000)" 100 loops, best of 5: 12.8 msec per loop
# cProfile.run('sum_min_max2(10)') 1    0.000    0.000    0.000    0.000 task1.py:53(sum_min_max2)
# cProfile.run('sum_min_max2(100)') 1    0.000    0.000    0.000    0.000 task1.py:53(sum_min_max2)
# cProfile.run('sum_min_max2(1000)') 1    0.000    0.000    0.002    0.002 task1.py:53(sum_min_max2)
# cProfile.run('sum_min_max2(10000)') 1    0.000    0.000    0.021    0.021 task1.py:53(sum_min_max2)


# 3. Вариант

def sum_min_max3(l):

    array = [random.randint(0, l * l) for _ in range(l)]

    idx_min = 0
    idx_max = 0
    for i in range(1, len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min
    summ = 0
    for i in range(idx_min + 1, idx_max):
        summ += array[i]

# "task1.sum_min_max3(10)" 100 loops, best of 5: 14 usec per loop
# "task1.sum_min_max3(100)" 100 loops, best of 5: 141 usec per loop
# "task1.sum_min_max3(1000)" 100 loops, best of 5: 1.33 msec per loop
# "task1.sum_min_max3(10000)" 100 loops, best of 5: 13.8 msec per loop
# cProfile.run('sum_min_max3(10)')  1    0.000    0.000    0.000    0.000 task1.py:76(sum_min_max3)
# cProfile.run('sum_min_max3(100)')  1    0.000    0.000    0.000    0.000 task1.py:76(sum_min_max3)
# cProfile.run('sum_min_max3(1000)') 1    0.000    0.000    0.003    0.003 task1.py:76(sum_min_max3)
# cProfile.run('sum_min_max3(10000)')  1    0.002    0.002    0.022    0.022 task1.py:76(sum_min_max3)

cProfile.run('sum_min_max3(10000)')

# Все алгоритмы при профилировании показали примерно одинаковые значения.
