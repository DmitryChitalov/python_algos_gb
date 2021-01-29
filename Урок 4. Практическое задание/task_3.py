"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit

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


enter_num = 1984584984958986848485869858585757567375474747474747473747477272737470293498575646463636363636

def main():
    res_1 = revers(enter_num)
    res_2 = revers_2(enter_num)
    res_3 = revers_3(enter_num)

print(timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=1000))
print(timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=1000))
print(timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=1000))

cProfile.run('main()')

# Так как операции быстрые, сложно сравнить алгоритмы в через cProfile.
# Зато через timeit видно, что методы строк гораздо быстрее, чем рекурсия и циклы.



