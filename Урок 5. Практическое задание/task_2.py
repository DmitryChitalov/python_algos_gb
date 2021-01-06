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
from collections import deque


def get_list(a1):
    return list(deque(a1))


def get_deci(a1):
    return list(map(lambda x: int(x, 16), a1))


def get_str(a1):
    my_hex = ''.join(a1)
    return my_hex


def get_hex(a1):
    return list(map(lambda x: format(x, 'x'), a1))


def summ_hex(a1, a2):
    return get_list(format((int(get_str(a1), 16) + int(get_str(a2), 16)), 'x'))


def mult_hex(a1, a2):
    return get_list(format((int(get_str(a1), 16) * int(get_str(a2), 16)), 'x'))


def get_summ(a1, a2):
    a1 = get_deci(a1)
    a2 = get_deci(a2)
    result_summ = []
    rank = 0
    for i in range((max(len(a1), len(a2))) + 1):
        flag = 0
        try:
            el1 = a1.pop()
        except IndexError:
            el1 = 0
            flag += 1
        try:
            el2 = a2.pop()
        except IndexError:
            el2 = 0
            flag += 1
        el_summ = el1 + el2 + rank
        rank = 0
        if el_summ > 15:
            rank = el_summ // 16
            el_summ = el_summ % 16
        result_summ.insert(0, el_summ)
    if flag > 2 and rank != 0:
        result_summ.insert(0, rank)
    if result_summ[0] == 0:
        result_summ.pop(0)  # костыль от первого нуля
    return list(map(lambda x: format(x, 'x'), result_summ))


def get_mult(a1, a2, mult=[], counter=0):
    for counter in range(int(get_str(a1), 16)):
        mult = get_summ(mult, a2)
    return mult


if __name__ == '__main__':
    # first = get_list(input('Введите шестнадцатиричное число: '))
    # second = get_list(input('Введите шестнадцатиричное число: '))
    first = get_list('A2')
    second = get_list('C4F')

    # # Чит-вариант:
    # print(summ_hex(first,second))
    # print(mult_hex(first, second))
    # # строго говоря в тз не сказано что мы должны делать вычисления с массивами - нужно умножать и складывать
    # # шестнадцатеричные числа, и хранить их в виде массива.
    # #
    # # нормальный вариант:

    print(get_summ(first, second))
    print(get_mult(first, second))
