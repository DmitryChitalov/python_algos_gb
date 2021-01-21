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

first_number = list(input("Введите первое число: "))
second_number = list(input("Введите второе число: "))

first_default_dict = defaultdict(int)
second_default_dict = defaultdict(int)

for el in first_number:
    first_default_dict[el] = el

for el in second_number:
    second_default_dict[el] = el


def get_number(your_dict):
    if len(your_dict) == 1:
        return str(your_dict.popitem()[1])
    return str(your_dict.popitem()[1]) + get_number(your_dict)


x = get_number(first_default_dict)
y = get_number(second_default_dict)

x = x[::-1]
y = y[::-1]

overall_sum = hex(int(x, 16) + int(y, 16))
overall_mul = hex(int(x, 16) * int(y, 16))

print("Сумма равна:", [x.upper() for x in list(overall_sum)[2:]])
print("Произведение равно:", [x.upper() for x in list(overall_mul)[2:]])
