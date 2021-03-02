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
import collections


def calc():
    val_1 = input("введиите первое число в 16ричном формате: ")
    val_2 = input("введиите второе число в 16ричном формате: ")

    dicts = collections.defaultdict(list)

    dicts["1"] = list(val_1)
    dicts["2"] = list(val_2)

    result_dict = collections.defaultdict(list)

    summ_16 = dec_to_base(int(val_1, 16) + int(val_2, 16), 16)
    multipl_16 = dec_to_base(int(val_1, 16) * int(val_2, 16), 16)

    result_dict["1"] = list(summ_16)
    result_dict["2"] = list(multipl_16)

    print(f"сумма чисел: {result_dict['1']}")
    print(f"произведение чисел: {result_dict['2']}")


def dec_to_base(n, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEF'
    x, y = divmod(n, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else \
        dec_to_base.table[y]


calc()
