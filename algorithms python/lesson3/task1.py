lst1 = [i for i in range(2, 100)]
lst2 = [i for i in range(2, 10)]
summ = [0] * len(lst2)
for i in range(len(lst2)):
    for j in range(len(lst1)):
        if lst1[j] % lst2[i] == 0:
            summ[i] += 1
    print(f'{lst2[i]} кратно {summ[i]} чисел из диапазона')



