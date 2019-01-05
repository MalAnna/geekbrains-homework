print('Введите две латинские буквы в одном регистре:')
let1 = ord(input('let1 = '))
let2 = ord(input('let2 = '))

if 65 <= let1 <= 90 and 65 <= let2 <= 90:
    pos1 = let1 - 64
    pos2 = let2 - 64
    count = abs(pos1 - pos2) - 1
    print(f'Позиция первой буквы: {pos1}, позиция второй буквы: {pos2}, между ними {count} букв(а)')
elif 97 <= let1 <= 122 and 97 <= let2 <= 122:
    pos1 = let1 - 96
    pos2 = let2 - 96
    count = abs(pos1 - pos2) - 1
    print(f'Позиция первой буквы: {pos1}, позиция второй буквы: {pos2}, между ними {count} букв(а)')
else:
    print('Символы не соответствует буквам латинского алфавита')




