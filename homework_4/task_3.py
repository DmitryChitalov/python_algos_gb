"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import timeit

enter_num = 135792468

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main(enter_num):
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)

cProfile.run('main(enter_num)')

print(timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num"))
print(timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num"))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num"))

"""Вызов cProfile.run почему-то не обнаружил слабых мест в программе. Зато timeit дал ожидаемые результаты. 
Рекурсивная функция традиционно выполняется дольше остальных функций, поскольку она сохраняет результаты каждого
вложенного вызова в стеке. Цикл выполняется немного быстрее, поскольку не содержит вложенных циклов и выполнает 
простейшие операции. И последняя функция в разы быстрее, поскольку все, что она делает - это преобразует число в
строку и выполняет срез в обратном порядке символов. Единственное что надо добавить к ней, это обратное преобразование
в целое число, поскольку она, в отличии от других функций возвращает строку."""