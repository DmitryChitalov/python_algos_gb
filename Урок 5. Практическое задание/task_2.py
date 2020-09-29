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

x = 'A2'
y = 'C4F'


def num(x, y):
    l = max(len(x), len(y))
    num1 = deque(['0' for i in range(l + 1)], l + 1)
    for i in range(len(x)):
        num1.append(x[i])
    num2 = deque(['0' for i in range(l + 1)], l + 1)
    for i in range(len(y)):
        num2.append(y[i])
    return num1, num2


num1, num2 = num(x, y)


def sum_hex(x, y):
    num1, num2 = x, y
    k = 0
    result = ['0' for i in range(len(num1))]
    for i in range(len(num1)-1, -1, -1):
        result[i] = hex((int(num1[i], 16) + int(num2[i], 16) + k) % 16)[-1]
        if int(num1[i], 16) + int(num2[i], 16) >= 16:
            k = 1
        else:
            k = 0
    return result


def mul_hex(x, y):
    num1, num2 = x, y
    k = int(''.join(num1), 16)
    result = ['0' for i in range(max(len(num1), len(num2)) * 2)]
    n = deque(list(num2))
    while len(n) != len(result):
        n.appendleft('0')
    for i in range(1, k):
        result = sum_hex(result, n)
    return result


"""Это задание не сделано, не хватило времени"""