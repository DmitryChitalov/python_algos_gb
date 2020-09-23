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

from hashlib import sha1


def substring_qty(data):
    res = set()
    char_pos = 0
    while char_pos < len(data):
        substring_len = 1
        while substring_len < len(data):
            res.add(sha1(data[char_pos:char_pos + substring_len].encode('utf-8')).hexdigest())
            substring_len += 1
        char_pos += 1

    return len(res)


if __name__ == '__main__':
    print(f'Количество уникальных подстрок = {substring_qty(input("Задайте строку: "))}')
