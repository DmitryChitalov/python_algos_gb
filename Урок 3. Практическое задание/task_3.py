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


import hashlib


def count_unique_sub_str(word):
    unique_sub_str = set()
    for i in range(len(word)+1):
        for j in range(i+1, len(word)+1):
            sub_str_hash = hashlib.sha1(word[i:j].encode()).hexdigest()
            print(word[i:j])
            unique_sub_str.add(sub_str_hash)
    print(f'В слове \"{word}\" уникальных подстрок - {len(unique_sub_str)-1}')


count_unique_sub_str('qwe')
