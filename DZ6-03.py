# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


  ## НАЧАЛЬНЫЙ ВАРИАНТ ##
# list = [2.321, 1.2, 3.1111, 5.002, 10.1]
# new_list = []
# for i in range(len(list)):
#     if list[i] % 1 != 0:
#         new_list.append(list[i])
# x2 = [round(new_list[i] % 1, 3) for i in range(len(new_list))]
# print(f"{x2} => {max(x2) - min(x2)}")


   ## НОВОЕ РЕШЕНИЕ ##
import random
list = [round(random.uniform(0,10),3) for x in range(5)]
nl = [round(list[i] % 1, 3) for i in range(len(list))]
print(f"{nl} => {max(nl) - min(nl)}")
