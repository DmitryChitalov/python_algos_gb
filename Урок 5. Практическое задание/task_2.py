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
from collections import namedtuple


def sum_hex(a, b):
    Number16 = namedtuple('Number16', 'num num_list')
    a_tuple = Number16(num=a, num_list=list(a))
    b_tuple = Number16(num=b, num_list=list(b))
    t_sum = str(hex(int(a_tuple.num, 16) + int(b_tuple.num, 16))).upper()[2:]
    c_tuple = Number16(num=t_sum, num_list=list(t_sum))
    print(f"Сумма чисел {a_tuple.num_list} и {b_tuple.num_list} равна {c_tuple.num_list}")


def mult_hex(a, b):
    Number16 = namedtuple('Number16', 'num num_list')
    a_tuple = Number16(num=a, num_list=list(a))
    b_tuple = Number16(num=b, num_list=list(b))
    t_sum = str(hex(int(a_tuple.num, 16) * int(b_tuple.num, 16))).upper()[2:]
    c_tuple = Number16(num=t_sum, num_list=list(t_sum))
    print(f"Произведение чисел {a_tuple.num_list} и {b_tuple.num_list} равна {c_tuple.num_list}")


if __name__ == "__main__":
    a = input("Введите 1-е число: ")
    b = input("Введите 2-е число: ")

    sum_hex(a, b)
    mult_hex(a, b)
