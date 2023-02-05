# Задача 3. Реализуйте алгоритм перемешивания списка. 
#НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
#максимум использование библиотеки Random для получения случайного int.

import random

def mix_list(list_original): 
    list = list_original[:]                                     # Создаем копию, поскольку мы не должны изменять оригинал
    list_length = len(list)                                     # Цикл от 0 до длины списка -1
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)     # Получение случайного индекса
        temp = list[i]                                          # Замена
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list                                                 # Возвращаем список

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mixed_list = mix_list(list)
print('Исходный список: ')
print(list)
print('Перемешанный список: ')
print(mixed_list)
