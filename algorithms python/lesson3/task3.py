import random

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

print(lst)
print(max_, pos_max)
print(min_, pos_min)

lst[pos_max] = min_
lst[pos_min] = max_

print(lst)