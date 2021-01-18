"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import defaultdict

number_1 = input('Введите 1 шестнадцатеричное число: ')
number_2 = input('Введите 2 шестнадцатеричное число: ')

lst_1 = [el for el in number_1]
n = len(lst_1) - 1
num_1 = 0
for el in lst_1:
    num_1 += int(el, 16) * (16**n)
    n -= 1

lst_2 = [el for el in number_2]
n = len(lst_2) - 1
num_2 = 0
for el in lst_2:
    num_2 += int(el, 16) * (16**n)
    n -= 1

my_dict = defaultdict(list)

my_dict[number_1] = num_1
my_dict[number_2] = num_2

sum_lst = []
for el in hex(my_dict[number_1] + my_dict[number_2]):
    sum_lst.append(el.upper())

mul_lst = []
for el in hex(my_dict[number_1] * my_dict[number_2]):
    mul_lst.append(el.upper())

print(f'Сумма чисел из примера: {sum_lst[2:]}, произведение - {mul_lst[2:]}.')