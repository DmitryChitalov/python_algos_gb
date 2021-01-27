"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""
from collections import defaultdict

numbers = defaultdict(list)
a = input('Введите число в шестнадцатеричном формате: ')
numbers['first'].extend(a)
b = input('Введите число в шестнадцатеричном формате: ')
numbers['second'].extend(b)
print(numbers)
multipl = int(''.join(numbers['first']), 16) * int(''.join(numbers['second']), 16)
summ = int(''.join(numbers['first']), 16) + int(''.join(numbers['second']), 16)
result = defaultdict(list)
result['mul'].extend(hex(multipl).split('x')[1])
result['sum'].extend(hex(summ).split('x')[1])
print(f'Произведение: {result["mul"]}, сумма: {result["sum"]}')
