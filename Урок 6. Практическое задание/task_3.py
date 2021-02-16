"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


def oddeven(digit, odd=0, even=0):
    if digit != 0:
        if digit % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        digit = digit // 10
        return oddeven(digit, odd, even)
    else:
        return even, odd
@profile
def my_func(number):
    return oddeven(number)


print(my_func(10032334034534534662372367834834234543534032456985769459840))

#На каждый рекрсинный вызов функции создается отдельный замер.
#Для решения проблемы, сделаем вызов рекурсии из другой функции и сделаем замер для нее.