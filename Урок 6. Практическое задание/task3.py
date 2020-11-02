""""
Задание 3 *.
Сделайте профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни' в профилировании
python 3.8.2
Windows 10 64 bit
"""

from memory_profiler import profile

number_str = '1000878700000'


@profile
def revers_all(number_str):
    def revers_number2(number_str2):
        if len(number_str2) == 1:
            return number_str2
        else:
            return number_str2[len(number_str2) - 1] + revers_number2(number_str2[:(len(number_str2) - 1)])
    revers_number2(number_str)


if __name__ == '__main__':
    print(f'{revers_all(number_str)}')

"""
Особенность профелирования рекурсии, она вызывает сама себя и каждый вызов  при использовании @profile замеряется
отдельно. Для того что бы этого избежать нужно функцию с рекурсией обернуть еще в одну функцию.
"""