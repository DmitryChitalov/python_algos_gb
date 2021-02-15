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
# Lesson_2 Task_2  (подсчет четных и нечетных значений в числе)
from memory_profiler import profile


@profile
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


@profile
def count_even_odd_2_for_if_enum(num, even=0, odd=0):  # уходим от рекурсии
    str_num = str(num)
    for _, num in enumerate(str_num):  # используем enumerate(str_num)
        if (int(num) % 10 % 2) == 0:  # int(num)
            even += 1
        else:
            odd += 1
    return even, odd


@profile
def count_even_odd_3_for_if_map(num, even=0, odd=0):
    str_num = str(num)
    new_list = map(int, str_num)  # map вместо int(num)
    for num in new_list:  # for in вместо enumerate(str_num)
        if (num % 10 % 2) == 0:
            even += 1
        else:
            odd += 1
    return even, odd


@profile
def count_even_odd_4_while(num, even=0, odd=0):
    while num:  # вместо прохода по всем цифрам сокращаем начальное число
        if (num % 10 % 2) == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd


new_num = 345123456434567345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734519098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234345123456713456789098734512345643456734512345671345678909873451234564345673498734512345643456734512345671345678909873451234564345673498734512345643456734512345671345678909873451234564345673498734512345643456734512345671345678909873451234564345673498734512345643456734512345671345678909873451234564345673498734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567890987

# count_even_odd_1_recursion(new_num)
# рекурсия вообще решить задачу не может, что делает просто её непригодной для больших данных
count_even_odd_2_for_if_enum(new_num)  # даже на больших данных Increment не показал увеличение памяти
count_even_odd_3_for_if_map(new_num)
# в данном случае функция map не дала дала увеличения памяти, так же profile не показал разницы между
# проходом по списку через for in и for in с использованием функции enumerate
count_even_odd_4_while(new_num)


# в четвертом случае произошло увеличение памяти дважды, за счет того, что мы считаем все значение дважды,
# а не отдельную цифру как в прошлых вариантах, что говорит о том, что не стоит использовать данный метод

def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def count_even_odd_5_recursion(num, even=0, odd=0):
    if (num % 10 % 2) == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
    if num == 0:
        return even, odd
    else:
        return count_even_odd_5_recursion(num, even, odd)


new_num = 345123456434567345123456713456789098734512345643456734512345671345678909873451234564345673451234567134567893451234564345673451234567134567890987345123456434567345123456713456789098734512345643456734512345671345678934512345643456734512345671345678909873451234564345673451234567134567890987345123456434567345123456713456789
print(count_even_odd_5_recursion(new_num))

# так же к одному из способов оптимизации функций можно отнести мемоизацию, что в разы увеличит скорость её выполнения
# т.к. мы освобождаемся от необходимости персчитывать уже полученные значения
# тем не менее мы продолжаем быть зависимы ограничением количеством вызываемых рекурсий


'''
Вывод:
1. рекурсия непригодна для больших данных в связи с системным ограничением на кол-во рекурсий
так же рекурсия тратит огромное количество памяти
2. между for in и for in enumerate нет разницы
3. не всегда map даёт уменьшение памяти, при использовании необходимо смотреть на её целесообразность
4. четвертый вариант так же является менее оптимальным т.к. идёт двойной расчёт всех данных
5. так же к 7му способов оптимизации памяти можно было бы отнести мемоизацию памяти в рекурсиях, она позволяет в разы
увеличить расчёт (к сожалению но не избавляет от ограничений по рекурсиям)
'''
