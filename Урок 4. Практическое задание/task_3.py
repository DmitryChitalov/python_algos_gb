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


# print(revers(123456))
# print(revers_2(123456))
# print(revers_3(123456))

cProfile.run('revers(123456)')
"""в данном случае из выведенных результатов видно, что в функции revers(123456) 10 вызовов: 4 из них не были вызваны 
рекурсией, а 6 остальных- рекурсивные вызовы. Затраты времени cumtime- 0.000 
"""
cProfile.run('revers_2(123456)')
"""в функции revers_2(123456)- 4 вызова, затраты времени cumtime- 0.000"""
cProfile.run('revers_3(123456)')
"""в функции revers_3(123456)- также 4 вызова, затраты также показывают cumtime- 0.000 """
# замеры с помощью cProfile показывают, что в функциях нет потерь времени

print(timeit.timeit('lambda: revers(123456)',
                    setup='from __main__ import revers',
                    number=10000))
print(timeit.timeit('lambda: revers_2(123456)',
                    setup='from __main__ import revers',
                    number=10000))
print(timeit.timeit('lambda: revers_3(123456)',
                    setup='from __main__ import revers',
                    number=10000))
#  исользуя timeit, видно, что функция reverse_3 работает побыстрее, т. к. срезы- встроенный метод