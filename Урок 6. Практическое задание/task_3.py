"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""

'''
Как и было отмечено, на уроке, если профилировать функцию рекурсию, то будет столько же
выведено таблиц, сколько будет запусков функции. Чтобы была одна таблица, я вложил 
вложил функцию-рекурсию в обычную функцию main. И уже по функции main профилировал.
'''

from memory_profiler import profile


def reverse_number(my_list, rev_num=None):
    if rev_num is None:
        rev_num = []
    if len(my_list) == 0:
        new_num = ''.join(rev_num)
        print(new_num)
        return
    else:
        rev_num.append(my_list.pop())
        return reverse_number(my_list, rev_num)


@profile
def main():
    reverse_number(my_list)


my_list = (list(input('Введите номер, который требуется перевернуть ')))
main()
