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


def sum(x, y):
    perenos = 0
    result = deque()
    if len(x) > len(y):
        x, y = deque(x), deque(y)
    else:
        x, y = deque(y), deque(x)

    while x:
        if y:
            res = HEX_TO_NUM[x.pop()] + HEX_TO_NUM[y.pop()] + perenos
        else:
            res = HEX_TO_NUM[x.pop()] + perenos

        perenos = 0

        if res > 16:
            result.appendleft(NUM_TO_HEX[res - 16])
            perenos = 1
        else:
            result.appendleft(NUM_TO_HEX[res])
    if perenos != 0:
        result.appendleft('1')
    return result


def mul(x, y):
    result = deque()
    x, y = deque(x), deque(y)

    sdvig = 0
    perenos = 0
    while y:
        n = y.pop()
        x_copy = x.copy()
        i = 0
        while x_copy:
            m = x_copy.pop()
            res = HEX_TO_NUM[n] * HEX_TO_NUM[m] + perenos
            perenos = res // 16
            if perenos > 0:
                res = res - 16 * perenos
            if sdvig == 0:
                result.appendleft(NUM_TO_HEX[res])
            else:
                k = len(result) - 1 - sdvig - i
                if k < 0:
                    result.appendleft(NUM_TO_HEX[res])
                else:
                    m = HEX_TO_NUM[result[k]] + res
                    perenos = perenos + m // 16
                    m = m - (m // 16 * 16)
                    result[k] = NUM_TO_HEX[m]
            i = i + 1

        result.appendleft(NUM_TO_HEX[perenos])

        perenos = 0
        sdvig = sdvig + 1
    return result


HEX_TO_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
              'F': 15}

NUM_TO_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
              7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D',
              14: 'E',
              15: 'F'}

num_1 = list(input('Введите 1-е шестнадцатиричное число: ').upper())
num_2 = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(sum(num_1, num_2))
print(mul(num_1, num_2))

# не придумал как тут использовать defaultDict, поэтому использовал deque
