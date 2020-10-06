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


def summ_and_mult_hex():
    n1 = int(input('input number 1: '))
    n2 = int(input('input number 2: '))

    res_sum = []
    res_mult = []

    summery = n1 + n2
    multuply = n1 * n2
    for el in hex(summery):
        res_sum.append(el)
    for el in hex(multuply):
        res_mult.append(el)

    s_list = []
    s_list2 = []

    for el in hex(n1):
        s_list.append(el)

    for el in hex(n2):
        s_list2.append(el)

    d = defaultdict(list)
    d[n1] = s_list
    d[n2] = s_list2
    return f'{d}, сумма = {res_sum}, произведение = {res_mult}'


print(summ_and_mult_hex())
# с задание справился быстро( в Вы говорили,что самое сложное) поэтому думаю,что сделано неправильно)
