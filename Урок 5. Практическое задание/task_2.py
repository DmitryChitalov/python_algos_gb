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
from functools import reduce
from collections import defaultdict, deque

h_nums = '0123456789ABCDEF'


def check_num(h_number):
    if len(h_number) == 0:
        return False
    for el in h_number:
        if el not in h_nums:
            return False
    return True


def conv_to_dict(num_list):
    num_dict = defaultdict(int)
    num_list.reverse()
    for i, el in enumerate(num_list):
        num_dict[i] = el
    return num_dict


def calc_sum(n1, n2):
    a1 = conv_to_dict(n1)
    a2 = conv_to_dict(n2)
    num = len(n1) if len(n1) > len(n2) else len(n2)
    res = deque()
    p = 0
    for i in range(num + 1):
        s = int(str(a1[i]), 16) + int(str(a2[i]), 16) + p
        p = s // 16
        res.append(h_nums[s % 16])
    res.reverse()
    while res[0] == '0' and len(res) > 1:
        res.popleft()
    return res


def calc_mul(n1, n2):
    a1 = conv_to_dict(n1)
    a2 = conv_to_dict(n2)
    mult = []
    for i in range(len(n1)):
        p = 0
        pr = deque()
        for j in range(len(n2) + 1):
            k = int(str(a1[i]), 16) * int(str(a2[j]), 16) + p
            p = k // 16
            pr.append(h_nums[k % 16])
        for z in range(i):
            pr.appendleft('0')
        pr.reverse()
        mult.append(pr)
    return reduce(calc_sum, mult)


while True:
    user_ans = input('Введите * - для умножения, + - для сложения, 0 - для выхода: ')
    if user_ans == 0:
        break
    if user_ans in '*+':
        while True:
            num1 = list(input('Введите первое число: ').strip())
            num2 = list(input('Введите второе число: ').strip())
            if check_num(num1) and check_num(num2):
                break
            else:
                print('Ошибка ввода! Попробуйте ещё раз')
        if user_ans == '+':
            print(f'{num1} + {num2} = ')
            print(list(calc_sum(num1, num2)))
        else:
            print(f'{num1} * {num2} = ')
            print(list(calc_mul(num1, num2)))
    else:
        print('Ошибка ввода! Попробуйте ещё раз')
