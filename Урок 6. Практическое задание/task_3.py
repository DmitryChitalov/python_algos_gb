"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def recursion(number):
    last_num = number % 10
    number //= 10

    if number == 0:
        return last_num

    return int(str(last_num) + str(recursion(number)))


print(recursion(123))

"""
При профилировании рекурсий выходная таблица анализа будет появляться столько раз, сколько циклов рекурсии произошло.
Например, в данном примере было 3 цикла, а значит будет и 3 таблицы.
"""


@profile
def recursion_2(number):
    def in_recursion(num):
        last_num = num % 10
        num //= 10

        if num == 0:
            return last_num

        return int(str(last_num) + str(in_recursion(num)))

    return in_recursion(number)


print(recursion_2(123))

"""
Вторая функция не имеет рекурсии, но имеет вложенную  рекурсивную функцию, и поэтому основная функции профилируется только 1 раз.
"""
