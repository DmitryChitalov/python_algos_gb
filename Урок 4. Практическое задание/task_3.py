"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run

def revers(enter_num, revers_num=0):
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
@@ -33,4 +37,65 @@ def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
#############################################################

def lambda_reverse(num): # используем lambda
    return num[::-1]
lambda_reverse = lambda num: num[::-1]


num=124585685020982893989131290134748974892891276383489349
num_str=str(num)
print("revers_1", timeit('revers_1(num)', setup='from __main__ import revers_1, num', number=10000))
print("revers_2", timeit('revers_2(num)', setup='from __main__ import revers_2, num', number=10000))
print("revers_3", timeit('revers_3(num)', setup='from __main__ import revers_3, num', number=10000))
print("lambda_reverse", timeit('lambda_reverse(num_str)', setup='from __main__ import lambda_reverse, num_str', number=10000))

def main_start_revers1():
    num = 124585685020982893989131290134748974892891276383489349
    revers_1(num)

def main_start_revers2():
    num = 124585685020982893989131290134748974892891276383489349
    revers_2(num)

def main_start_revers3():
    num = 124585685020982893989131290134748974892891276383489349
    revers_3(num)

def main_start_lambda_reverse():
    num = str(124585685020982893989131290134748974892891276383489349)
    lambda_reverse(num)

print("-------------------------------------------------------")
print("cProfile revers_1")
run('main_start_revers1()')

print("-------------------------------------------------------")
print("cProfile revers_2")
run('main_start_revers2()')

print("-------------------------------------------------------")
print("cProfile revers_3")
run('main_start_revers3()')

print("-------------------------------------------------------")
print("cProfile lambda_reverse")
run('main_start_lambda_reverse()')


"""
revers_1 0.23600490000000002
revers_2 0.17336639999999998
revers_3 0.006726799999999977
lambda_reverse 0.002650799999999953
reverse_1 самый неээфективный: он самый медленный, а также в нем используется больше всех вызовов
из-за проверки значения (if)   
    cProfile revers_1
             59 function calls (5 primitive calls) in 0.000 seconds
быстрее всех из предложенных - revers_3: в нем нет никаких расчетов, используется индекс у строки
"""