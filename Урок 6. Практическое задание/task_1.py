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
import memory_profiler
from random import randint
import time

# задача на разворот функции
num_100 = randint(10000, 1000000)


def reverse(number):
    res = 0
    for i in range(number):
        res += (number % 10) * 10
        number = number // 10
    return res

    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def rev(num):
    res = 0
    for i in range(len(str(num))):
        digit = num % 10
        num = num // 10
        res = res * 10
        res = res + digit
    return res


def rev_lst(num):
    num = str(num)
    n_list = list(num)
    n_list.reverse()
    n2 = "".join(n_list)
    return n2


def rev_str(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


if __name__ == '__main__':
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    print(reverse(num_100))
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    print(rev(num_100))
    t3 = time.process_time()
    m3 = memory_profiler.memory_usage()
    print(rev_lst(num_100))
    t4 = time.process_time()
    m4 = memory_profiler.memory_usage()
    print(rev_str(num_100))
    t5 = time.process_time()
    m5 = memory_profiler.memory_usage()

    time_diff1 = t2 - t1
    time_diff2 = t3 - t2
    time_diff3 = t4 - t3
    time_diff4 = t5 - t4
    mem_dif1 = m2[0] - m1[0]
    mem_dif2 = m3[0] - m2[0]
    mem_dif3 = m4[0] - m3[0]
    mem_dif4 = m5[0] - m4[0]

    print(f'Время на первую функцию:{time_diff1}, затраты памяти  {mem_dif1} MB')
    print(f'Время на вторую функцию:{time_diff2}, затраты памяти  {mem_dif2} MB')
    print(f'Время на третью функцию:{time_diff3}, затраты памяти  {mem_dif3} MB')
    print(f'Время на чектвертую функцию:{time_diff4}, затраты памяти  {mem_dif4} MB')

# скрипты не затратны по памяти, "узких мест" нет
# Python 3.7, разрядность ОС 64
