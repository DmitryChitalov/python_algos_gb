"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile, pstats
import random
import timeit
import sys

sys.setrecursionlimit(1000000)


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

rand_num = int(''.join([str(random.randrange(0, 10)) for _ in range(100)]))

profiler = cProfile.Profile()
profiler.enable()
print(revers(rand_num))
print(revers_2(rand_num))
print(revers_3(rand_num))
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('tottime')
stats.print_stats()

print('revers()\t--\t',
    timeit.timeit(
        'revers(rand_num)',
        setup='from __main__ import revers, rand_num',
        number=10000))
print('revers_2()\t--\t',
    timeit.timeit(
        'revers_2(rand_num)',
        setup='from __main__ import revers_2, rand_num',
        number=10000))
print('revers_3()\t--\t',
    timeit.timeit(
        'revers_3(rand_num)',
        setup='from __main__ import revers_3, rand_num',
        number=10000))


'''
По выполнению данной задачи видно что cProfile позволяет определить затраты времени за 1 прогон
Однако если значения будут крайне малы для 1го запуска, данные окажутся бесполезными (нулевыми)
В свою очередь timeit позволяет оценивать затратность на время исполнения кода при больших нагрузках,
как если бы запрос шёл от 100, 1000 или любого другого значения пользователей в один момент
Таким образом, если я имею дело со сложным кодом, который выполняет большое число операций - cProfile
Если же я оцениваю оптимальность кода для высоконагруженных систем - timeit
'''