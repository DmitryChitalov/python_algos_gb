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
input_str = input("Введите строку:")

substrings = set()
for i in range(len(input_str)):
    for j in range(i, len(input_str)):
        substr = input_str[i:j+1]
        if substr == input_str:
            continue
        substring_hash = hashlib.sha256(substr.encode()).hexdigest()
        if substring_hash not in substrings:
            print(substr)
            substrings.add(substring_hash)


count_str = len(substrings)
print(
    f"Количество различных подстрок в строке '{input_str}' составляет: {count_str}")
#
