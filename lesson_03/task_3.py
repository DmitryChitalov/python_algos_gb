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


def substr_count(user_str):
    substr_set = set()
    for length in range(1, len(user_str)):
        for idx in range(len(user_str)):
            substr_hash = hash(user_str[idx:idx + length])
            substr_set.add(substr_hash)
    return len(substr_set)


test_list = ['papa', 'mom', 'brother', 'sister', 'grandmother']

for item in test_list:
    print(f'Количество подстрок в строке {item}: {substr_count(item)}')
