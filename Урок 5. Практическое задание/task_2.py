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


def make_dict(nums):
    my_dict = defaultdict(str)
    for n, i in enumerate(nums):
        my_dict[n] = i
    return my_dict


number_1 = input('Введите первое число в шестнадцатиричной системе (например А2): ')
number_2 = input('Введите второе число в шестнадцатиричной системе (например C4F): ')

dict_number_1 = make_dict(number_1)
dict_number_2 = make_dict(number_2)
sum_nums = hex(int(number_1, 16) + int(number_2, 16))
mult_nums = hex(int(number_1, 16) * int(number_2, 16))
dict_sum = make_dict(sum_nums[2:].upper())
dict_mult = make_dict(mult_nums[2:].upper())

print(f'Вы ввели числа {list(dict_number_1.values())} и {list(dict_number_2.values())}\n'
      f'Сумма этих чисел равна {list(dict_sum.values())}\n'
      f'Произведение этих чисел равно {list(dict_mult.values())}')
