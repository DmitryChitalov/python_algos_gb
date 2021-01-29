"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
import cProfile
from memory_profiler import profile


@profile
def reverso(number):
    if len(number) == 1:
        return number[0]
    else:
        return reverso(number[1:]) + number[0]


user_number = input("Введите число ")
print(reverso(user_number))


@profile
def just_reverse(number):
    return ''.join(reversed(number))


user_number = input("Введите число ")
print(just_reverse(user_number))

"""
Каждый вызов рекурсивной функции отображается в консоли и 
сохраняется в стеке вызовов, задействуя все больше и больше памяти
"""