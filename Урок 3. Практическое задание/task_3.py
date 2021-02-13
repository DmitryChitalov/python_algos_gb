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

###########################################################
input_string = input("Entrer a string: ")
unique_str_set = set()

N = len(input_string)

for i in range(N):
    if i == 0:
        N = len(input_string) - 1
    else:
        N = len(input_string)
    for j in range(N, i, -1):
        unique_str_set.add(hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest())
print(f"Totally  {len(unique_str_set)} unique substrings in {input_string}")
