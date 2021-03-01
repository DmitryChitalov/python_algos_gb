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
from hashlib import md5

substrings1 = set()  # для записи подстрок преобразованных в хеш
substrings2 = set()  # для записи обычных подстрок


def get_substrings(i_string: str):
    for i in range(1, len(i_string)+1):
        substrings1.add(md5(i_string[:i].encode("utf-8")).hexdigest())
        substrings2.add(i_string[:i])


string = input("Введите строку для поиска всех возможных подстрок: ")

# в каждой след итерации отсекаем по первому элменту.
for idx in range(0, len(string)+1):
    get_substrings(string[idx:])

print(len(substrings1))
print(substrings1)

print(len(substrings2))
print(substrings2)
