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


def calc_substrings(input_string):
    substrings = set()
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            substring = input_string[i:j+1]
            if substring == input_string:
                continue
            substring_hash = hashlib.sha256(substring.encode()).hexdigest()
            if substring_hash not in substrings:
                print(substring)
                substrings.add(substring_hash)
    return len(substrings)


in_str = input("Введите строку:")
print(f"Количество различных подстрок в строке {in_str} составляет: {calc_substrings(in_str)}")
