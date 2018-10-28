import random

print('Введите диапазон целых чисел:')
int1 = int(input('int1 = '))
int2 = int(input('int2 = '))

print('Введите диапазон вещественных чисел:')
float1 = float(input('float1 = '))
float2 = float(input('float2 = '))

print('Введите диапазон символов:')
simb1 = ord(input('simb1 = '))
simb2 = ord(input('simb2 = '))

print(f'Случайное целое число в диапазоне от {int1} до {int2}:')
print(f'{random.randint(int1,int2)}')

print(f'Случайное вещественное число в диапазоне от {float1} до {float2}:')
print(f'{random.uniform(float1,float2)}')

print(f'Случайный симвод в диапазоне от {chr(simb1)} до {chr(simb2)}:')
print(f'{chr(random.randint(simb1,simb2))}')
