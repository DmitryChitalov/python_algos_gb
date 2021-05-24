"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


def recursive(num):
    global even, odd
    if num == 0:
        return
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    a = num // 10
    recursive(a)


@profile(precision=4)
def recursive_wrapper(a):
    return recursive(a)


a = int(input('Введите длинное число:   '))

even = 0
odd = 0

recursive_wrapper(a)
print(f"Четных: {even}, нечетных: {odd}")

"""
профайлер будет запускаться столько раз сколько будет запускать себя рекурсивная функция
для избежания этого нужна другая функция запускающая рекурсию
"""

