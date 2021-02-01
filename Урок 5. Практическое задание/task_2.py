"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля
collections
Для лучшее освоения материала можете даже сделать несколько решений этого
задания, применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши
знания по ООП (в частности по перегрузке методов)
"""
from collections import defaultdict


def sum_hex(f_num, s_num):
    check_string = '0123456789ABCDEF'
    res = defaultdict(list)

    f_num = [c for c in f_num]
    s_num = [c for c in s_num]
    if len(f_num) < len(s_num):
        f_num, s_num = s_num, f_num
    k = 0
    for i in range(len(s_num)):
        idx = - i - 1
        fst = check_string.index(f_num[idx])
        snd = check_string.index(s_num[idx])
        k, m = divmod(fst + snd + k, 16)
        res[i] = check_string[m]

    for i in range(len(s_num), len(f_num)):
        idx = - i - 1
        num = check_string.index(f_num[idx])
        k, m = divmod(num + k, 16)
        res[i] = check_string[m]
        if i == len(f_num) + 1:
            if k != 0:
                res[i + 1] = check_string[k]
    result = [res[k] for k in range(len(res) - 1, -1, -1)]
    return result


def mul_hex(f_num, s_num):
    check_string = '0123456789ABCDEF'
    res = defaultdict(list)

    f_num = [c for c in f_num]
    s_num = [c for c in s_num]
    if len(f_num) < len(s_num):
        f_num, s_num = s_num, f_num
    k = 0
    result_string = ''
    for s in s_num[::-1]:
        for f in f_num[::-1]:
            idx = (len(f_num) - 1) - f_num.index(f)
            fst = check_string.index(f)
            snd = check_string.index(s)
            k, m = divmod(fst * snd + k, 16)
            res[idx] = check_string[m]
            if len(f_num) - 1 == idx:
                while k != 0:
                    res[idx + 1] = check_string[k % 16]
                    k = k // 16
                    idx += 1
        add_str = '0' * (len(s_num) - 1 - s_num.index(s))
        result = [str(res[k]) for k in range(len(res) - 1, -1, -1)]
        result_string = sum_hex(result_string, f"{''.join(result)}{add_str}")
    return result_string


first = 'A2'
second = 'C4F'

print(sum_hex(first, second))
print(mul_hex(first, second))
