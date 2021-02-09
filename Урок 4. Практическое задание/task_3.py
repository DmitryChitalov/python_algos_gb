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


nums = int(input("Введите число:"))

print(timeit("revers(nums)", globals=globals(), number=1000))
print(timeit("revers_2(nums)", globals=globals(), number=1000))
print(timeit("revers_3(nums)", globals=globals(), number=1000))

# Рекурсия самый медленный способ решения + требует больше памяти т.к. нужно хранить стек вызовов.
# Обход в цикле быстрее.
# Использвание среза самый быстрый способ.

cProfile.run("revers(nums)")
cProfile.run("revers_2(nums)")
cProfile.run("revers_3(nums)")
