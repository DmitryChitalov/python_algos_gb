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


def determine_different_substrings(word):
    result = set()
    for i in range(len(word)):
        for j in range(len(word), i, -1):
            hash_str = hashlib.sha256(word[i:j].encode('utf-8')).hexdigest()
            result.add(hash_str)
    return print(f'В строке {word} - {len(result) - 1} различных подсрок')


if __name__ == "__main__":
    my_word = input('Введите строку состоящую только из строчных латинских букв: ')
    determine_different_substrings(my_word)
