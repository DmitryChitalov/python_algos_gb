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
# """
# Python 3.8.0 win 64x
# Lesson_2 Task_2
from sys import getsizeof
from pympler import asizeof

new_num = 345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987


def count_even_odd_1_recursion(num, even=0, odd=0):
    if (num % 10 % 2) == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
    if num == 0:
        return even, odd
    else:
        return count_even_odd_1_recursion(num, even, odd)  # рекурсия


def count_even_odd_2_for_if_enum(num, even=0, odd=0):  # уходим от рекурсии
    str_num = str(num)
    for _, num in enumerate(str_num):  # используем enumerate(str_num)
        if (int(num) % 10 % 2) == 0:  # int(num)
            even += 1
        else:
            odd += 1
    return even, odd


def count_even_odd_3_for_if_map(num, even=0, odd=0):
    str_num = str(num)
    new_list = map(int, str_num)  # map вместо int(num)
    for num in new_list:  # for in вместо enumerate(str_num)
        if (num % 10 % 2) == 0:
            even += 1
        else:
            odd += 1
    return even, odd


def count_even_odd_4_while(num, even=0, odd=0):
    while num:  # вместо прохода по всем цифрам сокращаем начальное число
        if (num % 10 % 2) == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


print(getsizeof(count_even_odd_1_recursion(new_num)))  # 28
print(asizeof.asizeof(count_even_odd_1_recursion(new_num)))  # 64
print(getsizeof(count_even_odd_2_for_if_enum(new_num)))  # 28
print(asizeof.asizeof(count_even_odd_2_for_if_enum(new_num)))  # 64
print(getsizeof(count_even_odd_3_for_if_map(new_num)))  # 28
print(asizeof.asizeof(count_even_odd_3_for_if_map(new_num)))  # 64
print(getsizeof(count_even_odd_4_while(new_num)))  # 28
print(asizeof.asizeof(count_even_odd_4_while(new_num)))  # 64

'''
даже на больших данных все расчёты показали один и тот же объём занимаемой памяти
вывод:
в данном случае getsizeof и asizeof беполезны, воспользуемся profile из memory_profiler
'''
