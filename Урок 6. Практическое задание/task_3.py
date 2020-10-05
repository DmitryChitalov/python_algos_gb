"""
Сделать профилировку для скриптов с рекурсией, ответить на вопросы "можно ли так профилировать" и "есть ли подводные
камни?"
"""

from memory_profiler import profile


@profile(precision=9)
def sum_calculate(user_num, start=1, my_sum=0):
    if user_num == start:
        my_sum += start
        formula = int(user_num * (user_num + 1) / 2)
        if my_sum == formula:
            return True
        else:
            return False
    else:
        my_sum += start
        return sum_calculate(user_num, start + 1, my_sum)


print(sum_calculate(20))

"""
Вывод последних трёх измерений: 
Line #    Mem usage    Increment   Line Contents
================================================
    10  13.203125000 MiB  13.179687500 MiB   @profile(precision=9)
    11                             def sum_calculate(user_num, start=1, my_sum=0):
    12  13.203125000 MiB   0.000000000 MiB       if user_num == start:
    13  13.203125000 MiB   0.000000000 MiB           my_sum += start
    14  13.203125000 MiB   0.000000000 MiB           formula = int(user_num * (user_num + 1) / 2)
    15  13.203125000 MiB   0.000000000 MiB           if my_sum == formula:
    16  13.207031250 MiB   0.003906250 MiB               return True
    17                                     else:
    18                                         return False
    19                                 else:
    20  13.195312500 MiB   0.000000000 MiB           my_sum += start
    21  13.234375000 MiB   0.027343750 MiB           return sum_calculate(user_num, start + 1, my_sum)


Filename: C:/Users/NPC/PycharmProjects/pythonProject/lesson_6/task_3.py

Line #    Mem usage    Increment   Line Contents
================================================
    10  13.203125000 MiB  13.179687500 MiB   @profile(precision=9)
    11                             def sum_calculate(user_num, start=1, my_sum=0):
    12  13.203125000 MiB   0.000000000 MiB       if user_num == start:
    13  13.203125000 MiB   0.000000000 MiB           my_sum += start
    14  13.203125000 MiB   0.000000000 MiB           formula = int(user_num * (user_num + 1) / 2)
    15  13.203125000 MiB   0.000000000 MiB           if my_sum == formula:
    16  13.207031250 MiB   0.003906250 MiB               return True
    17                                     else:
    18                                         return False
    19                                 else:
    20  13.195312500 MiB   0.000000000 MiB           my_sum += start
    21  13.234375000 MiB   0.027343750 MiB           return sum_calculate(user_num, start + 1, my_sum)


Filename: C:/Users/NPC/PycharmProjects/pythonProject/lesson_6/task_3.py

Line #    Mem usage    Increment   Line Contents
================================================
    10  13.203125000 MiB  13.179687500 MiB   @profile(precision=9)
    11                             def sum_calculate(user_num, start=1, my_sum=0):
    12  13.203125000 MiB   0.000000000 MiB       if user_num == start:
    13  13.203125000 MiB   0.000000000 MiB           my_sum += start
    14  13.203125000 MiB   0.000000000 MiB           formula = int(user_num * (user_num + 1) / 2)
    15  13.203125000 MiB   0.000000000 MiB           if my_sum == formula:
    16  13.207031250 MiB   0.003906250 MiB               return True
    17                                     else:
    18                                         return False
    19                                 else:
    20  13.195312500 MiB   0.000000000 MiB           my_sum += start
    21  13.234375000 MiB   0.027343750 MiB           return sum_calculate(user_num, start + 1, my_sum)


Профилировать так можно. Подводный камень один - вызов декоратора происходит каждый раз, когда вызывается функция внутри
рекурсии, соответственно, сколько раз будет вызвана функция, сколько раз отработает декоратор.
Пробовал нагуглить решение - найти ничего не удалось, были какие-то сложные примеры изменения внутренностей 
memory_profiler, но, как мне думается, я довольно мало для этого знаю. 

Я увеличил параметр precision, чтобы посмотреть, изменяется ли использование памяти от вызова к вызову. Ответ: нет.
Следовательно, исходя из данного примера, каждый вызов функции внутри рекурсии отнимает одно и то же кол-во памяти, 
кроме самого первого, т.к. он, по факту, последний и 21 строчка кода для него выполняется другим условием.  
"""
