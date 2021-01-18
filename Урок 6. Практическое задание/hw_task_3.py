"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@profile
def reverse(number):
    def recursive_reverse_1(num):
        if num == 0:
            return str(num % 10)
        return f'{str(num % 10)}{recursive_reverse_1(num // 10)}'
    return recursive_reverse_1(number)


print(recursive_reverse(12345))
print(reverse(12345))
'''
Первая функция recursive_reverse(number) профилируется столько раз, сколько повторяется рекурсивный метод.
Вторая функция reverse(number) профилируется один раз, так как не содержит рекурсивного метода,
но имеет вложенную в себя рекурсивную функцию recursive_reverse_1(num)

Как я понял, так делать можно, но возникает вопрос. А если рекурсивная функция большая, то придется разбираться,
какие аргументы передать родительской функции.

Функции взяты с дз 4го урока. 
'''