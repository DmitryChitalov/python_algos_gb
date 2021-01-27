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
from cProfile import run
from timeit import timeit


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


def main():
    revers_1(1234555432166667645341874612345554321666676453418)
    revers_2(1234555432166667645341874612345554321666676453418)
    revers_3(1234555432166667645341874612345554321666676453418)


print(timeit("revers_1(123455543216666764)", globals=globals(), number=1000))
print(timeit("revers_2(123455543216666764)", globals=globals(), number=1000))
print(timeit("revers_3(123455543216666764)", globals=globals(), number=1000))
print(timeit("revers_1(12345554321666676453418746123)", globals=globals(), number=1000))
print(timeit("revers_2(12345554321666676453418746123)", globals=globals(), number=1000))
print(timeit("revers_3(12345554321666676453418746123)", globals=globals(), number=1000))
print(timeit("revers_1(1234555432166667645341874612345554321666676453418)", globals=globals(), number=1000))
print(timeit("revers_2(1234555432166667645341874612345554321666676453418)", globals=globals(), number=1000))
print(timeit("revers_3(1234555432166667645341874612345554321666676453418)", globals=globals(), number=1000))
run('main()')

'''
Самая быстрая реализация через использования среза на строке, там нет операций с числами, он более
оптимизирован, вариант с рекурсией самый медленный и неоптимизированный
*** при enter_num = 123455543216666764 и numbers = 1000:
  revers_1 = 0.006224199999999999
  revers_2 = 0.0043102
  revers_3 = 0.00048180000000000445
*** при enter_num = 12345554321666676453418746123 и numbers = 1000:
  revers_1 = 0.009890899999999994
  revers_2 = 0.0071824000000000054
  revers_3 = 0.0005383999999999944
*** при enter_num = 1234555432166667645341874612345554321666676453418 и numbers = 1000:
  revers_1 = 0.017949099999999996
  revers_2 = 0.012908199999999995
  revers_3 = 0.0007255000000000039
'''