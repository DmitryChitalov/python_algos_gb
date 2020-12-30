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


def split(word):
    return [char for char in word]


word = 'рара'


def make_substrings1(word):
    word_list = split(word)
    a = set(word)
    for n in range(len(word_list)):
        temp_word = word_list[n]
        for k in range(n + 1, len(word_list)):
            if k == n:
                continue
            temp_word += word_list[k]
            if len(temp_word) == len(word_list):
                continue
            a.add(temp_word)
    return a


def make_substrings2(word):
    word_list = split(word)
    a = {}
    for n in range(len(word_list)):
        temp_word = word_list[n]
        temp_word_hash = hashlib.sha256(temp_word.encode()).hexdigest()
        if temp_word_hash not in a:
            a[temp_word_hash] = temp_word
        for k in range(n + 1, len(word_list)):
            if k == n:
                continue
            temp_word += word_list[k]
            if len(temp_word) == len(word_list):
                continue
            temp_word_hash = hashlib.sha256(temp_word.encode()).hexdigest()
            if temp_word_hash not in a:
                a[temp_word_hash] = temp_word
    return a


print(make_substrings1(word))
print(make_substrings2(word))
