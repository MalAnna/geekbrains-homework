# 9.Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

total_summ = 0
print('Сколько чисел хотите вводить?')
count = int(input('count = '))

for i in range(1, count+1):
    print(f'Введите {i} число')
    num = int(input())
    temp_num = num
    summ = 0
    while num // 10 != 0:
        summ = num % 10 + summ
        num = num // 10
    temp_summ = num + summ

    if temp_summ > total_summ:
        total_summ = temp_summ
        total_num = temp_num
print(f'Наибольшая сумма цифр у числа {total_num}, равна{total_summ}')