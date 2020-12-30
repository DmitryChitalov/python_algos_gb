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

line = str(input('Введите строку: '))

print(f'Строка "{line}" имеет длину {len(line)} символов')

substring_set = set()
substring_dict = {}

for i in range(len(line)):
    for j in range(len(line)-1 if i == 0 else len(line), i, -1):
        substring_set.add(hash(line[i:j]))
        substring_dict[line[i:j]] = hash(line[i:j])

print(len(list(substring_dict.keys())), list(substring_dict.keys()))
print('Количество различных подстрок в этой строке:', len(substring_set))
