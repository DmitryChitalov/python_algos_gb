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

HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
HEX_NUM_RES = {
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

#Переводим в десятиричную систему и выводим число
def translit_10(lst):
    deq_10 = deque()
    degree = len(lst) - 1
    res = 0
    for i in lst:
        if degree >= 0:
            if i in HEX_NUM.keys():
                res = HEX_NUM[i] * (16 ** degree)
                deq_10.append(res)
                degree -= 1
            else:
                continue
        else:
            continue
    return sum(deq_10)

# Подготавливаем к переводу в 16-ричную систему
def translit_16(num):
    deq_16 = deque()
    q = num
    res_1 = q // 16
    while res_1 % 16 != 0:
        res_n = res_1 // 16
        res = res_1 % 16
        deq_16.appendleft(res)
        res_1 = res_n
    return deq_16

# Переводим в 16 и ричную систему
def trans(deq):
    res = []
    for i in deq:
        if i in HEX_NUM_RES.keys():
            res.append(HEX_NUM_RES[i])
    return res

x = list(input('Введите 1-е шестнадцатиричное число: ').upper())
y = list(input('Введите 2-е шестнадцатиричное число: ').upper())

composition_10 = translit_10(x) * translit_10(y)
amount_10 = translit_10(x) + translit_10(y)

composition_16 = translit_16(composition_10)
amount_16 = translit_16(amount_10)

print(f'сумма шестнадцатеричных чисел = {trans(amount_16)}')
print(f'Произведение шестнадцатеричных чисел = {trans(composition_16)}')