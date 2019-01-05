# 2.Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

odd, eve = 0, 0
print('Введите число:')
num = int(input('num = '))

while num // 10 != 0:
    rem_div = num % 10
    if rem_div % 2 == 0:
        eve = eve + 1
    else:
        odd = odd + 1
    num = num // 10

rem_div = num % 10
if rem_div % 2 == 0:
    eve = eve + 1
else:
    odd = odd + 1
print(f'В введенном вами числе {eve} четных цифр и {odd} нечетных цифр')