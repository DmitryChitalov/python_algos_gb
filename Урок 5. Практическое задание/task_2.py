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


number1 = input('Введите первое число: ')
number2 = input('Введите второе число: ')

result = defaultdict(list)
for i in number1:
    result[1].append(i)
for i in number2:
    result[2].append(i)

summ = hex(int(''.join(str(x) for x in result[1]), 16) + int(''.join(str(x) for x in result[2]), 16))
result['summ'] = list(str(summ)[2:].upper())

mul = hex(int(''.join(str(x) for x in result[1]), 16) * int(''.join(str(x) for x in result[2]), 16))
result['mul'] = list(str(mul)[2:].upper())
print(
    f'Первое число - {result[1]}\n'
    f'Второе число - {result[2]}\n'
    f"Сумма чисел - {result['summ']}\n"
    f"Произведение чисел - {result['mul']}"
)
