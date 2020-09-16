"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def calc_num(user_num):
    global summ
    global user_n
    if user_n != 0:
        summ = summ + float(user_num[0])
        user_n -= 1
        return calc_num(user_num[1:])
    else:
        return print('Сумма элементов:{0}'.format(summ))


global summ
global user_n
summ = 0

user_n = int(input('Введите количество элементов:'))
user_num = list(input('Введите числа через пробел').split())
calc_num(user_num)
