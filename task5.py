import random

LENG = 10

lst = [random.randint(-10, 10) for i in range(LENG)]
pos = 0
max_min = -10

for i in range(len(lst)):
    if max_min <= lst[i] < 0:
        if lst[i] > max_min:
            max_min = lst[i]
            pos = i

print(lst)
print(max_min, pos)
