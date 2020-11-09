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


def num_converter(number, in_count_sys, out_count_sys):
    DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    acc = 0
    for a in number:
        acc = acc * in_count_sys + DIGITS.find(a)
    while acc > 0:
        k = acc % out_count_sys
        result += DIGITS[k]
        acc = acc // out_count_sys
    return result[::-1]


first_num = deque((input('Введите первое шестнадцатеричное число: ')).upper())
second_num = deque((input('Введите второе шестнадцатеричное число: ')).upper())

hex_sum = int(num_converter(first_num, 16, 10)) + int(num_converter(second_num, 16, 10))
hex_multi = int(num_converter(first_num, 16, 10)) * int(num_converter(second_num, 16, 10))

print(f'Результат сложения чисел - {deque(num_converter(str(hex_sum), 10, 16))}')
print(f'Результат сложения чисел - {deque(num_converter(str(hex_multi), 10, 16))}')
