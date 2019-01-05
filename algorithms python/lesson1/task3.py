print('Введите координаты двух точек:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

if x1 != x2:

    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2

    print('Уравнение прямой, проходящей через эти точки:')
    print(f'y = {k}x + {b}')

else:
    print('Данная прямая параллельна оси OY, а ее уравнение можно записать в виде:')
    print(f'x = {x1}')