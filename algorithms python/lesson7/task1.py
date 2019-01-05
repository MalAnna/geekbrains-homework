# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами
#  на промежутке [-100; 100).
#  Вывести на экран исходный и отсортированный массивы.

from random import randrange


def bubble_sort(array):
    n = 1
    check_change = True

    while check_change:
        check_change = False

        for i in range(len(array) - n):

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                check_change = True
        n += 1
        #print(array)


leng = int(input('Введите количесво элементов в массиве: '))
array = [randrange(-100, 100) for i in range(leng)]
print(array)
#print('*' * 50)
bubble_sort(array)
#print('*' * 50)
print(array)
