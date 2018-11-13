import random

LENG = 10

lst = [random.randint(0, 100) for i in range(LENG)]
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

print(lst)
print(f'Максимальный элемент {max_}, его позиция {pos_max}, минимальный элемент {min_}, его позиция {pos_min}')
print(f'Между ними {abs(pos_min - pos_max)-1} элемента(ов)')

if pos_min < pos_max and pos_max - pos_min != 1:
    if pos_min + 1 == pos_max - 1:
        summ_ = lst[pos_min + 1]
    else:
        for i in range((pos_min + 1), pos_max):
            summ_ = summ_ + lst[i]
    print(f'Cумма элементов между ними {summ_}')
elif pos_min > pos_max and pos_min - pos_max != 1:
    if pos_min - 1 == pos_max + 1:
        summ_ = lst[pos_max + 1]
    else:
        for i in range((pos_max + 1), pos_min):
            summ_ = summ_ + lst[i]
    print(f'Cумма элементов между ними {summ_}')
else:
    print(f'Нет элементов между')