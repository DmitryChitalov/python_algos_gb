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

user_input = input('Text: ')
data = set()

count = len(user_input)
for i in range(count):
    if i == 0:
        count = len(user_input) - 1
    count = len(user_input)

    for el in range(count, i, -1):
        print(user_input[i:el])
        data.add(hashlib.sha256(user_input[i:el].encode('utf-8')).hexdigest())

print(data)
print(f'Уникальных элементов {len(data)}')