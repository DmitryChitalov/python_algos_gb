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

print('Пример 1')
enter_num = 123456
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)


print('Рекурсия: ', timeit(f'revers({enter_num})',
                                               setup='from __main__ import revers', number=10000))
print('Цикл: ', timeit(f'revers_2({enter_num})',
                                            setup='from __main__ import revers_2', number=10000))
print('Срез: ', timeit(f'revers_3({enter_num})',
                                            setup='from __main__ import revers_3', number=10000))

cProfile.run('revers(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

"""
Возможно три вида реализации задачи "число наоборот", самый быстрый вариант показала реализация
через срез, в связи с отсутствием арифметических действий. В данной задаче, использование этого
алгоритма наиболее оптимально

"""