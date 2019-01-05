# 8.Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра, которую
# необходимо посчитать, задаются вводом с клавиатуры.

digit_count = 0
print('Сколько чисел хотите вводить?')
count = int(input('count = '))
print('Какую цифру хотите найти?')
digit = int(input('digit = '))
for i in range(1, count+1):
    print(f'Введите {i} число')
    num = int(input())
    while num // 10 != 0:
        if num % 10 == digit:
            digit_count += 1
        num = num // 10
    if num == digit:
        digit_count += 1
print(f'Цифра {digit} найдена {digit_count} раз(а)')