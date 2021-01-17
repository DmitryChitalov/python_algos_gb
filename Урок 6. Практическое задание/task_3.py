"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

"""
В первоначальном коде с помощью рекурсии решалась задача подсчета четных и нечетных цифр в введенном числе.
При использовании профилировщика с рекурсией возвращается таблицы с результатом на каждый вызов функции самой себя.
Чтобы этого избежать, можно добавить внешнюю фнкцию и декоратор @profile использовать с внешеней фенкцией:
"""

from memory_profiler import profile
from random import randint

even_numbers = 0
odd_numbers = 0

@profile
def check_recursive_function():

    def odd_or_even_count(user_input, i):
        global even_numbers
        global odd_numbers
        if i != len(user_input):
            res = (int(user_input[i])) % 2
            if res == 0:
                even_numbers += 1
            else:
                odd_numbers += 1
            odd_or_even_count(user_input, i + 1)

    return odd_or_even_count(str(randint(0, 9000)), 0)


print(check_recursive_function())