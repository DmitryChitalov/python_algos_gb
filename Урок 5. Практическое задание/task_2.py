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

def summ_hex(a1,a2):
    return get_list(format((int(get_str(a1),16)+int(get_str(a2),16)),'x'))

def mult_hex(a1,a2):
    return get_list(format((int(get_str(a1),16)*int(get_str(a2),16)),'x'))


"""
# тут пытался реализовать поэлементное сложение 16-ричных чисел в массивах, но что-то зарылся и не получилось
def diff_rank(up_rank, result_summ, i=1):
    l = len(result_summ)
    if i <= l:
        n = l - i
        new_el = result_summ.pop(n) + up_rank
        if new_el > 15:
            up_rank = new_el // 16
            down_rank = new_el % 16
            result_summ.insert(n, down_rank)
            i += 1
            return diff_rank(up_rank, result_summ, i)
        else:
            result_summ.insert(n, new_el)
            return result_summ
    else:
        result_summ.insert(0, up_rank)
    return result_summ


def sum_list(a1, a2, result_summ=[]):
    # len_diff = len(a1) - len(a2)
    # if len_diff > 0:
    #     for i in range(len_diff):
    #         result_summ.append(a1.pop(i))
    #     return sum_list(a1, a2, result_summ)
    # elif len_diff < 0:
    #     for i in range(abs(len_diff)):
    #         result_summ.append(a2.pop(i))
    #     return sum_list(a1, a2, result_summ)
    # else:
    print(result_summ)

    for i in reversed(range(len(a1))):
        l = len(result_summ)-1 if len(result_summ) != 0 else 0
        up_rank = 0
        # print(a1, a2)
        my_summ = a1.pop() + a2.pop()
        print(my_summ)
        if my_summ < 15:
            result_summ.insert(i, my_summ)
        else:
            up_rank = my_summ // 16
            down_rank = my_summ % 16
            result_summ.append(down_rank)
            # print(result_summ)
            result_summ = diff_rank(up_rank, result_summ)
    return result_summ
"""

if __name__ == '__main__':
    # first = get_list(input('Введите шестнадцатиричное число: '))
    # second = get_list(input('Введите шестнадцатиричное число: '))
    first = get_list('A2')
    second = get_list('C4F')
    # second = get_list('eec')
    # first = get_list('111')
    # print(get_hex(get_deci(first)))
    # print(sum_list(get_deci(first), get_deci(second)))
    # print(diff_rank(1, get_deci(second)))
    # print(get_hex(first))
    print(summ_hex(first,second))
    print(mult_hex(first, second))


