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


def calc_numbs():
    numbs = defaultdict(list)
    for i in range(2):
        numb = input(f'Введите {i + 1} число: ')
        numbs[i + 1] = list(numb.upper())
    print(numbs)
    summ = int(''.join(numbs[1]), 16) + int(''.join(numbs[2]), 16)
    mult = int(''.join(numbs[1]), 16) * int(''.join(numbs[2]), 16)
    print(f'Сумма чисел равна {hex(summ)[2:]}')
    print(f'Произведение равно {hex(mult)[2:]}')


calc_numbs()
