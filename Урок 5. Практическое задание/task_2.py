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
from functools import reduce


def calc_by_lists(i_list1, i_list2):
    i_list1 = i_list1[::-1]
    ldd_num1 = defaultdict(int)
    for i in range(len(i_list1)):
        ldd_num1[i] = i_list1[i]

    i_list2 = i_list2[::-1]
    ldd_num2 = defaultdict(int)
    for i in range(len(i_list2)):
        ldd_num2[i] = i_list2[i]

    if(len(ldd_num1) > len(ldd_num2)):
        l_max_iter = ldd_num1.keys()
    else:
        l_max_iter = ldd_num2.keys()

    l_des_sum = reduce(lambda a, b: a + int(str(ldd_num1[b]), 16) * (16**b)
                                      + int(str(ldd_num2[b]), 16) * (16**b),
                       l_max_iter, 0)
    l_des_mul = 0
    for i in l_max_iter:
        l_cur_mul = int(str(ldd_num1[i]), 16) * (16**i)
        l_des_mul += reduce(lambda a, b: a + l_cur_mul
                                      * int(str(ldd_num2[b]), 16) * (16**b),
                            l_max_iter, 0)
    return list(str(hex(l_des_sum))[2:].upper()), list(str(hex(l_des_mul))[2:].upper())


gs_num1 = input('Введите первое шестнадцатиричное число: ')
gl_num1 = list(gs_num1)
gs_num2 = input('Введите второе шестнадцатиричное число: ')
gl_num2 = list(gs_num2)

g_nums = calc_by_lists(gl_num1, gl_num2)
print('Сумма данных чисел:', g_nums[0], '. Произведение данных чисел:', g_nums[1])
