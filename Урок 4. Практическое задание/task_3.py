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

0
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


cProfile.run("revers")
cProfile.run("revers_2")
cProfile.run("revers_3")
print(timeit.timeit('revers',setup='from __main__  import revers'))
print(timeit.timeit('revers_2',setup='from __main__  import revers_2'))
print(timeit.timeit('revers_3',setup='from __main__  import revers_3'))
"""
 в данном примере разница не такая большая ну в общем случаи здесь эффективнее 3 тий вариант рекурсия и цыкл работает медленнее
"""