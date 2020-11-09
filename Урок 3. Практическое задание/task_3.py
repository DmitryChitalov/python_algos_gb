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

"""Сделал двумя способами: 
1) через словарь без set
2) через лист с set"""

import hashlib

text = 'papa'

substrings_hash_dict = {}

for i in text:
    substrings_hash_dict[i] = hashlib.sha256(i.encode()).hexdigest()  # находим все одиночные подстроки

i = 1
text_rev = text[::-1]  # разворот строки
while i < len(text):
    head = text[i:]  # ищем подстроки с начала
    tail = text_rev[i:]  # ищем подстроки с конца
    substrings_hash_dict[head] = hashlib.sha256(head.encode()).hexdigest()
    # полученную с "хвоста" подстроку разворачиваем обратно
    substrings_hash_dict[tail[::-1]] = hashlib.sha256(tail[::-1].encode()).hexdigest()
    if tail in text:  # оставляем только существующие подстроки, т.к. при некоторых входных данных
        # образуются "развернутые" несуществующие подстроки (напр. тук --> ут)
        substrings_hash_dict[tail] = hashlib.sha256(tail.encode()).hexdigest()
    i += 1

print(f'Количество подстрок в слове {text}: {len(substrings_hash_dict)}\n')

for k, v in substrings_hash_dict.items():
    print(k, v)

"""Второй вариант"""


def substrings_hash(text):
    substrings_hash = []
    for i in text:
        substrings_hash.append(hashlib.sha256(i.encode()).hexdigest())
    i = 1
    text_rev = text[::-1]
    while i < len(text):
        head = text[i:]
        tail = text_rev[i:]
        substrings_hash.append(hashlib.sha256(head.encode()).hexdigest())
        substrings_hash.append(hashlib.sha256(tail[::-1].encode()).hexdigest())
        if tail in text:
            substrings_hash.append(hashlib.sha256(tail.encode()).hexdigest())
        i += 1

    return f'\nКоличество подстрок в слове {text}: {len(set(substrings_hash))}'


print(substrings_hash(text))
