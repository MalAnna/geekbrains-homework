# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
#  медианы, в другой – не больше ее.

import random


def find_median(array, leng):
    small = []
    medium = list(array)
    i = 0

    while i <= (leng // 2):
        small.append(min(medium))
        medium.pop(medium.index(min(medium)))
        i += 1
    print(small[-1])


leng = (2 * random.randint(5, 10)) + 1
array = [random.randint(0, 50) for i in range(leng)]
#print(array)
#print(sorted(array))
find_median(array, leng)
#print(array)
