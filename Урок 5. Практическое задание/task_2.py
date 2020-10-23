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

first_number = deque(input('Ввод первого числа: '))
second_number = deque(input('Ввод второго числа: '))
first_number = int(''.join(first_number), 16)
second_number = int(''.join(second_number), 16)
sum_of_numbers = hex(first_number + second_number).upper()
multiplication_of_numbers = hex(first_number * second_number).upper()
print(f'Сумма чисел из примера: {deque(sum_of_numbers[2:])}')
print(f'Произведение чисел из примера:{deque(multiplication_of_numbers[2:])}')
