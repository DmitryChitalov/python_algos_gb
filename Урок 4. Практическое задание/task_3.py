"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
"""
Введите пожалуйста произвольное число: 80137519875365917659125
Замер с помощью инструмента timeit 
revers 0.16138669999999955 seconds
revers_2 0.06287960000000048 seconds
revers_3 0.005424200000000212 seconds 

Видно, что в revers много лишних операций, а потому и время очень сильно просидает. 
memorise в данном задании не используется, но как мы могли убедиться в task_2 он был бы оптимальный.

Замер с помощью cProfile показался на данном примере не очень результативным.
По нулям. 
Как я поняла это очень удобный инструмент для анализа сложных алгоритмов - программ. 
С большим количеством вложенных функция. Для данного случая бессмысленен.
"""

from timeit import timeit
from cProfile import run


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


#  Эх! Тут есть такое решение :((( Я не оригинальна... :(
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def timeit_check():
    print("Замер с помощью инструмента timeit ")
    print(f"revers {timeit('revers(i_number)', globals=globals(), number=10000)} seconds")
    print(f"revers_2 {timeit('revers_2(i_number)', globals=globals(), number=10000)} seconds")
    print(f"revers_3 {timeit('revers_3(i_number)', globals=globals(), number=10000)} seconds")


def cprofile_check():
    revers(i_number)
    revers_2(i_number)
    revers_3(i_number)


i_number = int(input("Введите пожалуйста произвольное число: "))

timeit_check()
run('cprofile_check()')
