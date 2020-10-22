"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


"""
Результат:
Рекурсия: Память - 0.00390625

Цикл:
86     15.5 MiB     15.5 MiB           1   @profile
87                                         def calc_v2():
88                                             while True:
89     15.5 MiB      0.0 MiB           3           user_choose = input('Input operation (+, -, *, / or 0 to exit):')
90     15.5 MiB      0.0 MiB           3           if user_choose == '0':
91     15.5 MiB      0.0 MiB           1               break
92                                                 else:
93     15.5 MiB      0.0 MiB           2               try:
94     15.5 MiB      0.0 MiB           2                   a = int(input('Input first number: '))
95     15.5 MiB      0.0 MiB           2                   b = int(input('Input second number: '))
96                                                     except ValueError:
97                                                         print('Попробуйте ещё раз, скорей всего вы выели не число=)')
98     15.5 MiB      0.0 MiB           2               if user_choose == '+':
99     15.5 MiB      0.0 MiB           1                   print(f'Result = {a + b}')
100     15.5 MiB      0.0 MiB           1               elif user_choose == '-':
101                                                         print(f'Result = {a - b}')
102     15.5 MiB      0.0 MiB           1               elif user_choose == '*':
103                                                         print(f'Result = {a * b}')
104     15.5 MiB      0.0 MiB           1               elif user_choose == '/':
105                                                         print(f'Result = {a / b}')

Получилось прикольно, я не планировал решать подводные камни рекурсий в этом заднии.
Но почему-то выбрал пример именно с рекурсиией. И даже не дойдя до подводных камней я просто подумал много функций,
везде писать профайл это долго огромнный вывод получится просто сделаю отсечки. И только по ходу понял что решил 
проблему с замерами рекурсиси, в третем заднии какой-нибудь другой пример приведу.

Python 3.8 
OC x64
"""

import memory_profiler
from memory_profiler import profile


m1 = memory_profiler.memory_usage()


def sum(a: int, b: int) -> str:
    print('Ваш результат:', a + b)


def residual(a: int, b: int) -> str:
    print('Ваш результат:', a - b)


def multiplication(a: int, b: int) -> str:
    print('Ваш результат:', a * b)


def calc_devision(a: int, b: int) -> str:
    try:
        print('Ваш результат:', a / b)
    except ZeroDivisionError:
        print('Делит на ноль нельзя попрбуйте ещё раз!')
        rec_calc()


def rec_calc():
    operator_choose = input('Введите операцию (+, -, *, / или 0 для выхода):')
    if operator_choose == '0':
        return print('Вы завершили програму!')
    try:
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
    except ValueError:
        print('Попробуйте ещё раз, скорей всего вы выели не число=)')
        rec_calc()
    if operator_choose == '+':
        sum(a, b)
        rec_calc()
    elif operator_choose == '-':
        residual(a, b)
        rec_calc()
    elif operator_choose == '*':
        multiplication(a, b)
        rec_calc()
    elif operator_choose == '/':
        calc_devision(a, b)
        rec_calc()
    else:
        print('Вы вели не существующий знак, попробуйте ещё раз')
        rec_calc()


#rec_calc()

m2 = memory_profiler.memory_usage()


mem_diff = m2[0] - m1[0]

print(f'Память - {mem_diff}')


@profile
def calc_v2():
    while True:
        user_choose = input('Input operation (+, -, *, / or 0 to exit): ')
        if user_choose == '0':
            break
        else:
            try:
                a = int(input('Input first number: '))
                b = int(input('Input second number: '))
            except ValueError:
                print('Попробуйте ещё раз, скорей всего вы выели не число=)')
            if user_choose == '+':
                print(f'Result = {a + b}')
            elif user_choose == '-':
                print(f'Result = {a - b}')
            elif user_choose == '*':
                print(f'Result = {a * b}')
            elif user_choose == '/':
                print(f'Result = {a / b}')

calc_v2()
