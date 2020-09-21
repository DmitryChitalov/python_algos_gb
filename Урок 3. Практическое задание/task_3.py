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

string = input('Введите строку: ')

str_len = len(string)
sub_len = 1
substrings = []

while str_len > 0:
    for el in range(str_len):
        sub_1 = string[el:el + sub_len]
        sub = sha1(string[el:el + sub_len].encode('utf-8')).hexdigest()
        if sub not in substrings:
            substrings.append(sub)
        sub_len += 1
        str_len -= 1
        print(sub_1)
    print(f'В строке "{string}" {len(substrings)} подстрок')

