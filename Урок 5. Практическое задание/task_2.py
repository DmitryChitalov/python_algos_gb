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

user_number1 = input('Введите первое число в шестрадцатиричной форме:  ')
user_number2 = input('Введите второе число в шестрадцатиричной форме:  ')
# user_number1 = 'a2'
# user_number2 = 'c4f'
if len(user_number2) > len(user_number1):
    user_number1, user_number2 = user_number2, user_number1
user_list1 = list(user_number1.upper())
user_list2 = list(user_number2.upper())
user_deque1 = deque(user_list1)
user_deque2 = deque(user_list2)
user_deque3 = deque()
transfer = 0
for i in reversed(user_deque1):
    j = '0' if len(user_deque2) == 0 else user_deque2.pop()
    summ = int(i, 16) + int(j, 16) + transfer
    transfer = 1 if summ >= 16 else 0
    user_deque3.appendleft(format(summ - transfer * 16, 'X'))

if transfer > 0:
    user_deque3.appendleft(format(transfer, 'X'))

print(''.join(list(user_deque3)))

# К сожалению, я так замучила этот пример и зашла в тупик,
# что решила оставить на пока занятие по выяснению произведения...
