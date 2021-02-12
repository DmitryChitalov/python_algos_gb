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
from collections import defaultdict


def calculator():
    numbers = defaultdict(list)
    a = input('Введите первое число в шестнадцатеричной системе: ')
    numbers['first'].extend(a)
    b = input('Введите второе число в шестнадцатеричной системе: ')
    numbers['second'].extend(b)
    # print(numbers)
    mult = int(''.join(numbers['first']), 16) * int(''.join(numbers['second']), 16)
    summ = int(''.join(numbers['first']), 16) + int(''.join(numbers['second']), 16)
    result = defaultdict(list)
    result['mult'].extend(hex(mult).split('x')[1])
    result['summ'].extend(hex(summ).split('x')[1])
    print(f'Произведение: {result["mult"]}, сумма: {result["summ"]}')

calculator()


class Calculator:

    def __init__(self, first=input('Введите первое число в шестнадцатеричной системе: '), second=input('Введите второе число в шестнадцатеричной системе: ')):
        self.first = [i for i in first]
        self.second = [i for i in second]

    def __add__(self):
        result = list(hex(int(''.join(self.first), 16) + int(''.join(self.second), 16)))
        return result[2:]

    def __mul__(self):
        result = list(hex(int(''.join(self.first), 16) * int(''.join(self.second), 16)))
        return result[2:]


C_OBJ = Calculator()
print(C_OBJ.__add__())
print(C_OBJ.__mul__())
