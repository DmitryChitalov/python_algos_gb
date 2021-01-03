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
from functools import reduce


class HexNumbers:
    def __init__(self, num):
        self.num = num.upper()
        self.num_l = list(self.num)

    def __add__(self, other):
        total_sum = int(self.num, 16) + int(other.num, 16)
        total_sum = f'{total_sum:x}'
        return HexNumbers(total_sum)

    def __mul__(self, other):
        total_mul = int(self.num, 16) * int(other.num, 16)
        total_mul = f'{total_mul:x}'
        return HexNumbers(total_mul)


def numbers(first, second):
    numbs = defaultdict(list)
    [numbs[elem].extend(elem.upper()) for elem in [first, second]]
    sum_result = reduce((lambda x, y: int(x, 16) + int(y, 16)), numbs.keys())
    mul_result = reduce((lambda x, y: int(x, 16) * int(y, 16)), numbs.keys())
    numbs[sum_result].extend(f'{sum_result:X}'.upper())
    numbs[mul_result].extend(f'{mul_result:X}'.upper())
    print(f'Пользователь ввёл {first.upper()} и {second.upper()}. '
          f'Мы сохранили их как {numbs[first]} и {numbs[second]} соответственно.'
          f'\nСумма чисел пользователя: {numbs[sum_result]} , произведение - {numbs[mul_result]}.')


numbers(input('Введите первое шестнадцатеричное число: '), input('Введите второе шестнадцатеричное число: '))
print('--------- ООП решение -----------')
first_o = HexNumbers(input('Введите первое шестнадцатеричное число: '))
second_o = HexNumbers(input('Введите второе шестнадцатеричное число: '))
sum_hex = first_o + second_o
mul_hex = first_o * second_o
print(f'Пользователь ввёл {first_o.num} и {second_o.num}. '
      f'Мы сохранили их как {first_o.num_l} и {second_o.num_l} соответственно.'
      f'\nСумма чисел пользователя: {sum_hex.num_l} , произведение - {mul_hex.num_l}.')
