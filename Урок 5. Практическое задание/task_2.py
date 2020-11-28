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


def sum_mult_16(a, b):
    a = ''.join(a)
    b = ''.join(b)

    int_a = int(float.fromhex(a))
    int_b = int(float.fromhex(b))
    sum_int = int_a + int_b
    mul_int = int_a * int_b
    hex_sum = (hex(sum_int))[2:].upper()
    hex_mult = (hex(mul_int))[2:].upper()
    if len(hex_sum) % 2 == 1:
        hex_sum = f"0{hex_sum}"

    if len(hex_mult) % 2 == 1:
        hex_mult = f"0{hex_mult}"
    print(f"Сумма введенных чисел - {hex_sum}")
    print(f"Произведение введенных чисел - {hex_mult}")


first_num = deque(input('Введите первое число '))
second_num = deque(input('Введите второе число '))

sum_mult_16(first_num, second_num)
