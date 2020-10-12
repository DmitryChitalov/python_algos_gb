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


from memory_profiler import profile
from random import randint

# ЗАДАЧА ТАКАЯ:
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.

user_numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23,
                1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3,
                2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11,
                2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23,
                1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3,
                2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11,
                11, 9, 7, 2, 5, 6, 9, 22, 11, 90, 2, 12, 12, 9, 7, 2, 33, 78, 0, 9, 11, 20, 121, 2, 13, 1, 5 ]

list_1 = [randint(1, 1000) for i in range(100)]

# читерское решение через count


@profile
def function_1(user_list):
    result = [number for number in user_list if user_list.count(number) == 1]
    return result

# решение без count через словарь:


@profile
def function_2(user_list):
    dict_res = {}
    for number in user_list:
        dict_res.setdefault(number, 0)

    for number, count in dict_res.items():
        for i in range(len(user_list)):
            if number == user_list[i]:
                count += 1
                dict_res[number] = count
    result = [number for number in user_list if dict_res[number] == 1]
    return result

# тут не сильно наглядно, но получается, что через встроенные функции меньше памяти надо,
# чем если самому велосипед изобретать (даже если велосипед с list comprehension). Но инкермент так нигде и не появился

"""
Line #    Mem usage    Increment   Line Contents
================================================
    34     10.5 MiB     10.5 MiB   @profile
    35                             def function_1(user_list):
    36     10.5 MiB      0.0 MiB       result = [number for number in user_list if user_list.count(number) == 1]
    37     10.5 MiB      0.0 MiB       return result


Filename: /Users/Sergey/Desktop/algo_python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
    41     10.6 MiB     10.6 MiB   @profile
    42                             def function_2(user_list):
    43     10.6 MiB      0.0 MiB       dict_res = {}
    44     10.6 MiB      0.0 MiB       for number in user_list:
    45     10.6 MiB      0.0 MiB           dict_res.setdefault(number, 0)
    46                             
    47     10.6 MiB      0.0 MiB       for number, count in dict_res.items():
    48     10.6 MiB      0.0 MiB           for i in range(len(user_list)):
    49     10.6 MiB      0.0 MiB               if number == user_list[i]:
    50     10.6 MiB      0.0 MiB                   count += 1
    51     10.6 MiB      0.0 MiB                   dict_res[number] = count
    52     10.6 MiB      0.0 MiB       result = [number for number in user_list if dict_res[number] == 1]
    53     10.6 MiB      0.0 MiB       return result

"""
# ------------------------//------------------------------------------

# Что ж, попробуем еще пару примеров из курса алгоритмов (1 урок):

@profile
def min_element_from_list_1(user_list):
    for el in user_list:
        for idx in range(1, len(user_list)):
            if el < user_list[idx]:
                res = el
            else:
                res = user_list[idx]
            el = res
    return res


@profile
def min_element_from_list_2(user_list):
    min_element = user_list[0]
    for element in user_list:
        if element < min_element:
            min_element = element
    return min_element


@profile
def min_element_from_list_3(user_list):
    user_list.sort()
    return user_list[0]

# Тестируем на списке, список создаем через генератор

list_1 = [randint(1, 1000) for i in range(100)]

# примерно та же история - но сейчас все данные одинаковы. Инкеремент опять же не прибавляется.
# Ну, судя по всему, в этих участках кода с памятью работа идет оптимальным образом)))

"""
Line #    Mem usage    Increment   Line Contents
================================================
    96     10.7 MiB     10.7 MiB   @profile
    97                             def min_element_from_list_1(user_list):
    98     10.7 MiB      0.0 MiB       for el in user_list:
    99     10.7 MiB      0.0 MiB           for idx in range(1, len(user_list)):
   100     10.7 MiB      0.0 MiB               if el < user_list[idx]:
   101     10.7 MiB      0.0 MiB                   res = el
   102                                         else:
   103     10.7 MiB      0.0 MiB                   res = user_list[idx]
   104     10.7 MiB      0.0 MiB               el = res
   105     10.7 MiB      0.0 MiB       return res


Filename: /Users/Sergey/Desktop/algo_python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
   108     10.7 MiB     10.7 MiB   @profile
   109                             def min_element_from_list_2(user_list):
   110     10.7 MiB      0.0 MiB       min_element = user_list[0]
   111     10.7 MiB      0.0 MiB       for element in user_list:
   112     10.7 MiB      0.0 MiB           if element < min_element:
   113     10.7 MiB      0.0 MiB               min_element = element
   114     10.7 MiB      0.0 MiB       return min_element


Filename: /Users/Sergey/Desktop/algo_python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment   Line Contents
================================================
   117     10.7 MiB     10.7 MiB   @profile
   118                             def min_element_from_list_3(user_list):
   119     10.7 MiB      0.0 MiB       user_list.sort()
   120     10.7 MiB      0.0 MiB       return user_list[0]


"""


if __name__ == "__main__":
    function_1(user_numbers)
    function_2(user_numbers)
    print('------------------------------------')
    print('')
    min_element_from_list_1(list_1)
    min_element_from_list_2(list_1)
    min_element_from_list_3(list_1)

