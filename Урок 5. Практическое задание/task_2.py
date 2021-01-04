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


# Решение с использованием deque
def sum_hex(el1, el2):
    el1 = deque(el1)
    el2 = deque(el2)
    return deque(hex(sum([int(''.join(f'{el1.pop() if el1 else 0}{"0"*i}'), 16) +
                         int(''.join(f'{el2.pop() if el2 else 0}{"0"*i}'), 16)
                         for i in range(max(len(el1), len(el2)))])).lstrip('0x').upper())


def mult_hex(el1, el2):
    el2 = deque(el2)
    return deque(hex(sum([int(el1, 16) * int(''.join(f'{el2.pop()}{"0"*i}'), 16)
                          for i in range(len(el2))])).lstrip('0x').upper())


# Решение через ООП
class HexNumber:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return self.num.lstrip('0x').upper()

    def __add__(self, other):
        return HexNumber(hex(int(self.num, 16) + int(other.num, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.num, 16) * int(other.num, 16)))


if __name__ == '__main__':
    print('Решение с помощью deque:')
    s1 = 'A2'
    s2 = 'C4F'
    print(sum_hex(s1, s2))
    print(mult_hex(s1, s2))
    print('\nРешение через ООП:')
    a = HexNumber(s1)
    b = HexNumber(s2)
    print(a + b)
    c = a * b
    print(c)
