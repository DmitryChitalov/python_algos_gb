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

num_1 = deque(input('Введите первое число для сложения: '))
num_2 = deque(input('Введите второе число для сложения: '))
num_3 = deque(input('Введите первое число для умножения: '))
num_4 = deque(input('Введите второе число для умножения: '))

hex_sum = deque()


def addition_hex(a, b, transfer='0'):
    if len(a) == 0 and len(b) == 0:
        if transfer == '1':
            hex_sum.appendleft('1')
        return hex_sum
    key_a = '0' if len(a) == 0 else a.pop()
    key_b = '0' if len(b) == 0 else b.pop()
    formula_1 = hex(int(key_a, 16) + int(key_b, 16) + int(transfer, 16))
    integer_remainder = hex(int(formula_1, 16) % 16)[2:]
    transfer = '0' if hex(int(formula_1, 16) // 16) == '0x0' else '1'
    hex_sum.appendleft(integer_remainder.upper())
    return addition_hex(a, b, transfer)


print(addition_hex(num_1, num_2))


def func_2(a, b, multiplier=1):
    total_sum = ''
    subtotal = ''
    full_number = ''
    a = deque(a)
    b = deque(b)
    if len(a) < len(b):
        a, b = b, a
    if len(a) >= len(b):
        for i in range(len(a)):
            key_a = a.popleft()
            full_number += key_a
            a.append(key_a)
        for i in range(len(b)):
            key_b = b.pop()
            multiplication = (hex(int(full_number, 16) * int(key_b, 16) * int(multiplier)))[2:]
            b.appendleft(key_b)
            multiplier *= 16
            if i == 0:
                subtotal = multiplication
                total_sum = subtotal
            else:
                total_sum = addition_hex(deque(subtotal), deque(multiplication))
                subtotal = total_sum
    return total_sum


print(func_2(num_3, num_4))
