
"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

import timeit as t
from cProfile import run

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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

a = 654684649896416546516352186645146849846494654164894613231688446516484351349465489

print(t.timeit("revers_1(a)", globals=globals(), number=10000))
run('revers_1(a)')

print(t.timeit("revers_2(a)", globals=globals(), number=10000))
run('revers_2(a)')

print(t.timeit("revers_3(a)", globals=globals(), number=10000))
run('revers_3(a)')


"""
Принимая во внимание числы выведенные выше, наиболее оптимальным вариантом решения
будет третий вариант "переворота списка" с помощью которого будет затрачено наименее времени,
а также отсутствует большое количество вызовов функций как в первом варианте и не требует манипуляций
с дополнительными переменными как во втором варианте, что даст лучший результат в итоге.
"""