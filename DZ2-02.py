#Задача 2. Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
#Пример:  Для n=4 -> [2, 2.25, 2.37, 2.44]   Сумма 9.06

num = int(input('Ввеите число: '))

my_list = [(1+1/n)**n for n in range(1, num+1)]
print(f'Последовательность чисел при n = {num}:{my_list}\nСумма элементов списка: {round(sum(my_list), 2)}')
