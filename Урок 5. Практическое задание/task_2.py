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


class HexOperations:
    def __init__(self):
        self.first_number = list(
            input('Введите первое число в 16 системе счисления: ').upper())
        self.second_number = list(
            input('Введите второе число в 16 системе счисления: ').upper())
        self.result = None

    def __add__(self, other):
        self.result = list(hex(int((''.join(self.first_number)), 16) +
                               int((''.join(other)), 16)).upper()[2:])
        return self.result

    def __mul__(self, other):
        self.result = list(hex(int((''.join(self.first_number)), 16) *
                               int((''.join(other)), 16)).upper()[2:])
        return self.result


calc = HexOperations()
print(calc + calc.second_number)
print(calc * calc.second_number)

from collections import defaultdict


my_dict = defaultdict(list)
for i in range(1, 3):
    my_dict[i] = list(
            input('Введите число в 16 системе счисления: ').upper())
operation = input('Введите знак операции "+" или "*": ')
if operation == '*':
    result = list(hex(int((''.join(my_dict[1])), 16) *
             int((''.join(my_dict[2])), 16)).upper()[2:])
    print(result)
elif operation == '+':
    result = list(hex(int((''.join(my_dict[1])), 16) +
                      int((''.join(my_dict[2])), 16)).upper()[2:])
    print(result)
else:
    print('Введена неверная операция!')
