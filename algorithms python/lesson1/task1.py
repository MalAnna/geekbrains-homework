a = int(input('Введите трехзначное число: '))
b = a // 100 + a % 100 // 10 + a % 10
c = (a // 100) * (a % 100 // 10) * (a % 10)
print(f'Сумма цифр трехзначного числа: {b}, произведение цифр трехзначного числа: {c}')
