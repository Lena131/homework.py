# Задача 4. Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координаты точки А по оси х: '))
y1 = int(input('Введите координаты точки А по оси y: '))
x2 = int(input('Введите координаты точки B по оси х: '))
y2 = int(input('Введите координаты точки B по оси y: '))

import math
sqrt = math.sqrt(((x2 - x1)**2)+((y2 - y1)**2))
print(f'Расстояние между точами A и B = {sqrt}')
