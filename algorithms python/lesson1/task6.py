print('Введите номер буквы латинского алфавита:')
let = int(input('num = '))

if 1 <= let <= 26:
    pos = let + 64
    print(f'Это буква: {chr(pos)}')
else:
    print('В латинском алфавите 26 букв')