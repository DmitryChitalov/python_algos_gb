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


def get_from_user():
    hex_dict = defaultdict(list)
    hex_dict['first_num_hex'] = list(input("Введите первое число: "))
    hex_dict['second_num_hex'] = list(input("Введите второе число: "))
    return hex_dict


def sum_hex_func(h_dict_in):
    sum_hex = hex(int(''.join(h_dict_in['first_num_hex']), 16) + \
                  int(''.join(h_dict_in['second_num_hex']), 16))
    return list(sum_hex[2:])


def multiplication(h_dict_in):
    mult_hex = hex(int(''.join(h_dict_in['first_num_hex']), 16) * \
                   int(''.join(h_dict_in['second_num_hex']), 16))
    return list(mult_hex[2:])


num_h = get_from_user()
print(sum_hex_func(num_h))
print(multiplication(num_h))
