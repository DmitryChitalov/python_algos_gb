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
from timeit import Timer
import cProfile

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

######### My Variant ###########
def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = reversed(enter_num)
    return ''.join(revers_num)

print(revers_4(3215876543))

t1 = Timer('revers_1(3215876543)', globals=globals())
t2 = Timer('revers_2(3215876543)', globals=globals())
t3 = Timer('revers_3(3215876543)', globals=globals())
t4 = Timer('revers_4(3215876543)', globals=globals())
print("revers_1= ", t1.timeit(number=1000000))
print("revers_2= ", t2.timeit(number=1000000))
print("revers_3= ", t3.timeit(number=1000000))
print("revers_4= ", t4.timeit(number=1000000))

cProfile.run('revers_1(3215876543)')
cProfile.run('revers_2(3215876543)')
cProfile.run('revers_3(3215876543)')
cProfile.run('revers_4(3215876543)')




"""
----------Tests--------
----1-----number=1000000--------
-------enter_num = 321--------
revers_1=  0.5574196
revers_2=  0.40020370000000005
revers_3=  0.23281150000000006

----2-----number=10000000--------
-------enter_num = 321--------
revers_1=  5.776982599999999
revers_2=  4.037405199999999
revers_3=  2.337282

----3-----number=1000000--------
enter_num = 3215876543
revers_1=  1.7242937999999999
revers_2=  1.2242887
revers_3=  0.24959630000000033

----4-----number=10000000--------
enter_num = 3215876543
revers_1=  17.2048564
revers_2=  12.198058099999997
revers_3=  2.5041907000000023

----5-----number=10000000--------
enter_num = 3215876543
revers_1=  1.7353835
revers_2=  1.2250777
revers_3=  0.2515729000000002
revers_4=  0.5167965000000003

Мы видим, что revers_3 в разы быстрее остальных функций. В нем используются срезы. Очевидно, что они самые быстрые.
Плюс в самой функции кол-во операций меньше.
В revers_1 используется деление, это долгая операция. Так же здесь задействована рекурсия, мы видим, что этот
вариант самый долгий.
В revers_2 используется деление и цикл, но получается быстрее чем в revers_1. Потому что цикл быстрее рекурсии обычно

revers_4 работает быстрее 1 и 2, но в 2 раза медленнее revers_3.

cProfile показал только нули, тк функции короткие и видимо он на них не срабатываает, нужны более сложные 
участки кода.

"""