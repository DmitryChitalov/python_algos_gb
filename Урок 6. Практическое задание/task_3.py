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
    """
    Для рекурсивной функции определяем функцию-обертку, позволяющую произвести профилирование один раз.
    """

    def reversed_num(number, rev_number=[]):
        """
        Сформировать из введенного числа обратное по порядку входящих в него
        цифр и вывести на экран.
        """
        if number == 0:
            return ''.join(rev_number)
        rev_number.append(str(number % 10))
        return reversed_num(number // 10)

    return reversed_num(number)


recursion(16789)
'''
Для запуска программы было выделено 19.2 MiB.
По итогу инкремент отсутствует, поэтому оптимизация не требуется.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   116     19.2 MiB     19.2 MiB           1   @profile
   117                                         def recursion(number):
   118                                             """
   119                                             Для рекурсивной функции определяем функцию-обертку, позволяющую
                                                   произвести профилирование один раз.
   120                                             """
   121     19.2 MiB      0.0 MiB           7       def reversed_num(number, rev_number=[]):
   122                                                 """
   123                                                 Сформировать из введенного числа обратное по порядку входящих
                                                       в него цифр и вывести на экран
   124
   125                                                 """
   126     19.2 MiB      0.0 MiB           6           if number == 0:
   127     19.2 MiB      0.0 MiB           1               return ''.join(rev_number)
   128     19.2 MiB      0.0 MiB           5           rev_number.append(str(number % 10))
   129     19.2 MiB      0.0 MiB           5           return reversed_num(number // 10)
   130                                         
   131     19.2 MiB      0.0 MiB           1       return reversed_num(number)
'''
