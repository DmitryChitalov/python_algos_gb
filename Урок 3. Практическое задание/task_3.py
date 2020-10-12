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

def hash_creator(line: str):
    return hashlib.sha1(line.encode(encoding='UTF-8'))

def sub_line_searcher(main_line):
    subline_set = []
    step = 1
    while(step < len(main_line)):
        for itr in range(0, len(main_line)):
            subline_set.append(hash_creator(main_line[itr:itr + step]).hexdigest())
        step += 1
    return subline_set

line = str(input("Enter line: "))
sublines = sub_line_searcher(line)
print(set(sublines))