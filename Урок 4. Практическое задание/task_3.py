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

number = 949553865896535467657698786565
stmts = ('revers', 'revers_2', 'revers_3')

print('Проводим тесты с помощью timeit.')
for stmt in stmts:
    print(f'Алгоритм {stmt}:')
    print(timeit(f"{stmt}({number})",
                 setup=f'from __main__ import {stmt},'
                       f'number', number=10000))

print('Профилировка с помощью cProfile.')
for stmt in stmts:
    print(f'Алгоритм {stmt}:')
    print(cProfile.run(f'{stmt}({number})'))

"""
В функции revers нужно выполнять возврат return int(revers_num) в
базовом случае и возврат return revers(enter_num, revers_num) в основной
части рекурсии.
В функции revers_2 результат имеет тип float, что не соответствует
условию задачи. Можно исправить изменив вывод на return int(revers_num).

Алгоритм revers показывает самые плохие результаты, поскольку он
рекурсивный и обладает как низкой скоростью, так и высокими требованиями
к памяти.
Алгоритмы revers_2 и revers_3 имеют похожую сложность, однако:
- revers_2 должен на каждом шаге вычислять новое значение числа, что
занимает время и ресурсы процессора;
- revers_3 берёт срез от строки (где хэшируется как сама строка, так и
каждый её символ), что в итоге гарантирует очень высокую
производительность функции.
"""