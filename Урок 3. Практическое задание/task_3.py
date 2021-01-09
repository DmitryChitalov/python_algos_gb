import hashlib
"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""


def papa(string, start=0, end=1):       # изначально подстрока равна первому символу
    n = len(string)
    if start > n:                       # окончание рекурсии
        return string
    else:
        if end <= n:                            # пока правая граница не достигнет крайнего правого положения...
            substring = string[start:end]       # подстрока
            if len(substring) > 0 and substring != string:
                substring_hash = hashlib.sha256(substring.encode('utf-8')).hexdigest()    # хеширование
                set_res.add(substring_hash)                                             # добавление ко множеству
            return papa(string, start, end+1)       # ...рекурсивный вызов ф-ии с увеличением правой границы
        else:                                       # иначе...
            return papa(string, start+1, end=1)     # ...рекурсивный вызов ф-ии с увеличением левой границы,
                                                    # возвращение правой границы к первоначальному значению


string = input('Введите строку, состоящую только из строчных латинских букв: ').lower()
set_res = set()
papa(string)

for i, substring in enumerate(set_res, 1):          # вывод внесенных хешей
    print(f'{i}: {substring}')

print(f'{len(set_res)} - общее количество подстрок в строке <<{string}>>')
