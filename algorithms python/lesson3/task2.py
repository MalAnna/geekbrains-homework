import random

LENG = 10

lst1 = [random.randint(0, 100) for i in range(LENG)]
lst2 = []

for i in range(len(lst1)):
    if lst1[i] % 2 == 0:
        lst2.append(i)

print(lst1)
print(lst2)
