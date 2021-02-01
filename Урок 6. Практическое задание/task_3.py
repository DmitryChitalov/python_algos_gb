"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile

# профилировщик работает много раз
print('обычная рекурсия')
@profile
def my_string_old(string, list_hash=set()):
    if len(string) == 0:
        return list_hash
    else:
        n = len(string)
        while n != 0:
            b = string[:n]
            n -= 1
            res = hash(b)
            list_hash.add(res)
        return my_string_old(string[1:], list_hash)


my_string_old('papa')

# профилировщик сработал только раз
print('в декоратор передаем функцию')


def my_string(string, list_hash=set()):
    if len(string) == 0:
        return list_hash
    else:
        n = len(string)
        while n != 0:
            b = string[:n]
            n -= 1
            res = hash(b)
            list_hash.add(res)
        return my_string(string[1:], list_hash)


f1 = profile(my_string)
f1('papa')

'''
Если честно то вы сами подсказали такой метод написав что это очень просто. Я просто попробовал передать функцию в 
профилировщик и посмотрел результат, который так сказать "на лицо". Точно такой же как если использовать
синтаксический сахар. Я думаю что так можно профилировать
'''