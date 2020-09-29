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
from collections import namedtuple
hex_series = namedtuple('Hex', ['name', 'series'])


def concat_hex(arg1, arg2):
    result = [hex_series(name='A', series=list(arg1)),hex_series('B', list(arg2))]
    print(f'Произведение двух чисел {result[0].name} = {"".join(result[0].series)} и {result[1].name}'
          f' = {"".join(result[1].series)} равно '
          f'{(hex(int("".join(result[0].series),16) * int("".join(result[1].series),16)))[2:].upper() } ')

def mult_hex(arg1, arg2):
    result = [hex_series(name='A', series=list(arg1)), hex_series('B', list(arg2))]
    print(f'Сумма двух чисел {result[0].name} = {"".join(result[0].series)} и {result[1].name}'
          f' = {"".join(result[1].series)} равно '
         f'{(hex(int("".join(result[0].series),16) + int("".join(result[1].series),16)))[2:].upper() } ')

# print(a,b)
# print(hex(int(a,16)*int(b,16)))
concat_hex('d12','fde')
mult_hex('d12','fde')

print(hex(int('d12', 16) * int('fde', 16)))




