import random

LENG = 10

lst = [random.randint(0, 100) for i in range(LENG)]
count = 0
max_count = 0
num = -1

for i in range(len(lst) - 1):
    if lst[i] != num:
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count > max_count:
            max_count = count
            num = lst[i]
        count = 0

if num == -1:
    print(lst)
    print('В массиве нет повторяющихся элементов')
else:
    print(lst)
    print(f'Элемент {num} встречается в массиве чаще всего, {max_count + 1} раз')
