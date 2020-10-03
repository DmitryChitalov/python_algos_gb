"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
"""
Совместил 2 и 3 задание.
Во втором задании использовал генератор для оптимизации использования памяти.
К сожалению решение по очистке памяти после выполнения скрипта - DEL, пришло после разбора ДЗ на 7 лекции.
Но в случае с YIELD, считаю что чистка через DEL не обязательно, так как получить данные из генератора
можно только один раз.
"""

def Generator() :
    mylist = range(3)
    for i in mylist :
        yield i*i
mygenerator = Generator()
for i in mygenerator:
    print(i)

"""
Замеры выполнения рекурсии, поместил функцию с рекурсией в другую процедуру для получения общего результата
, а не результатов по каждой рекурсии.
"""
from memory_profiler import profile

@profile
def for_check(val_num):
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 2) + fib(n - 1)
    print(f'Result  {fib(val_num)}')

val_num = 5
for_check(val_num)
"""
Result  5
Filename: C:/Users/AlexT/PycharmProjects/pythonProject2/test_1.py

Line #    Mem usage    Increment   Line Contents
================================================
     3     13.7 MiB     13.7 MiB   @profile
     4                             def for_check(val_num):
     5     13.7 MiB      0.0 MiB       def fib(n):
     6     13.7 MiB      0.0 MiB           if n == 0 or n == 1:
     7     13.7 MiB      0.0 MiB               return n
     8                                     else:
     9     13.7 MiB      0.0 MiB               return fib(n - 2) + fib(n - 1)
    10     13.7 MiB      0.0 MiB       print(f'Result  {fib(val_num)}')
"""
