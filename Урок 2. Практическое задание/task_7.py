"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def calc_num(user_n):
    global summ
    global summ_1
    global count
    if count != 0:
        summ = summ + 1
        summ_1 = summ_1 + summ
        count -= 1
        return calc_num(count)
    else:
        return summ_1


global summ
global summ_1
global count
summ = 0
summ_1 = 0

user_n = int(input('Введите количество элементов:'))
count = user_n
if calc_num(user_n) == (user_n * (user_n + 1) / 2):
    print(True)
else:
    print(False)
