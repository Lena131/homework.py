# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
#Пример: если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
#НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ: Расширить значение коэффициентов до [-100..100]

k = int(input('Введите максимальное значение степени: '))
equetion = {}
import random
for i in range(k, -1, -1):
    equetion[i]= random.randint(-100,100)
print(equetion)

def write_file(eq_str):
    with open('Task01.txt', 'w') as data:
        data.write(eq_str)

eq_str = ''
for k, v in equetion.items():
    if k == 1:                                     #если степень =1, Vx
        eq_str+= f'{v}*x + '
    elif k==0:
        eq_str+= f'{v} + '                         #если степень=0, V (!!! по правилам =1)
    elif v==0:                                       
        eq_str-=f'{v}*x**{k} + '                   #если элемент =0, убираем выражение с х полностью
    elif v == 1:
        eq_str = eq_str-f'{v}*x**{k}' + f'x**{k}'  #если элемент =1, заменяем на x^  
    else:
        eq_str+= f'{v}*x**{k} + '                  #если степень >0, Vx^ 
else:
    eq_str = eq_str[:-2]

neq_str=''   
for v in eq_str:
    if v.startswith('-'):                          #если элемент с минусом, меняем "+-" на "-"
        neq_str=  eq_str.replace('+ -', '- ')     
    elif v.startswith('v'):
        neq_str = eq_str                           #иначе строка переписываеся без изенения

string_1=neq_str
str_dict = neq_str.replace(' ','').replace('+',' ').replace(',', '').replace('-',' -').replace('*x',':').replace('**','').split()
add=', '
jstr_dict=add.join(str_dict)   

print(eq_str,'= 0')   
print(string_1)
print(jstr_dict)


k2 = int(input('Введите максимальное значение степени: '))
equetion2 = {}
import random
for i in range(k2, -1, -1):
    equetion2[i]= random.randint(-100,100)
print(equetion2)

def write_file2(eq_str2):
    with open('Task02.txt', 'w') as data:
        data.write(eq_str2)

eq_str2 = ''
for k2, v2 in equetion2.items():
    if k2 == 1:
        eq_str2+= f'{v2}*x + '
    elif k2==0:
        eq_str2+= f'{v2} + '
    elif v2==0:                                       
        eq_str2-=f'{v2}*x**{k2} + '                  
    elif v2 == 1:
        eq_str2 +=f'x**{k2}'
    else:
        eq_str2+= f'{v2}*x**{k2} + '
else:
    eq_str2 = eq_str2[:-2]

neq_str2=''   
for v2 in eq_str2:
    if v2.startswith('-'):
        neq_str2=  eq_str2.replace('+ -', '- ')     
    elif v2.startswith('v2'):
        neq_str2 = eq_str2

string_2=neq_str2
str_dict2 = neq_str2.replace(' ','').replace('+',' ').replace(',', '').replace('-',' -').replace('*x',':').replace('**','').split()
add=', '
jstr_dict2=add.join(str_dict2)  

print(eq_str2,'= 0')   
print(string_2)
print(jstr_dict2)
