# homework.py
# Задачи после Урок 1. Знакомство с Python
*DZ-01. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет

*DZ-02. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

*DZ-03. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

*DZ-04. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
 
*DZ-05. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Задачи после Урок 2. Знакомство с Python. Продолжение
*DZ2-01. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
+ 6782 -> 23
+ 0,56 -> 11

*DZ2-02. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
Пример:
+ Для n=4 -> [2, 2.25, 2.37, 2.44]
+ Сумма 9.06

*DZ2-03. Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int

# Задачи после Урок 3. Данные, функции и модули в Python
*DZ3-01. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
Пример:
+ [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

*DZ3-02. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
+ [2, 3, 4, 5, 6] => [12, 15, 16];
+ [2, 3, 5, 6] => [12, 15]

*DZ3-03. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
Пример:
+ [1.1, 1.2, 3.1, 5, 10.01] => 0.19

*DZ3-04. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
+ 45 -> 101101
+ 3 -> 11
+ 2 -> 10

*DZ3-05. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
+ для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# Задачи после Урок 4. Данные, функции и модули в Python. Продолжение
*DZ4. A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
+ если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
Расширить значение коэффициентов до [-100..100]

# Задачи после Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

*DZ5-01. Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

+ a) Добавьте игру против бота
+ b) Подумайте как наделить бота 'интеллектом'

*DZ5-02. Создайте программу для игры в 'Крестики-нолики'
НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

*DZ5-03. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
+ aaaaabbbcccc -> 5a3b4c
+ 5a3b4c -> aaaaabbbcccc
