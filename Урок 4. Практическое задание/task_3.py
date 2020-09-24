"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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


"""
Функция revers() использует рекурсию, поэтому с точки зрения оптимизации менее эффективна.
А еще она не работала и возвращала None, поэтому пришлось дописать "return" и "revers_num".
Функция reverse_3() быстрее reverse_2(), т.к. вместо вычислений использует свойство строк в Python.
"""


result_1 = timeit("revers(205123)", "from __main__ import revers", number=100000)
result_2 = timeit("revers_2(205123)", "from __main__ import revers_2", number=100000)
result_3 = timeit("revers_3(205123)", "from __main__ import revers_3", number=100000)

print(f'Результат revers()  : {result_1}')
print(f'Результат revers_2(): {result_2}')
print(f'Результат revers_3(): {result_3}')
print()
cProfile.run('main(205123)')
