"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

inp_str = input("Введите слово из строчных латинских букв: ")
L = len(inp_str)
s = set()
s1 = set()

for i in range(L):
    if i == 0:
        L = len(inp_str) - 1
    else:
        L = len(inp_str)
    for j in range(L, i, -1):
        print(inp_str[i:j])
        print(inp_str[::-1][i:j])
        s.add(hash(inp_str[i:j].encode('utf-8')))
        s1.add(inp_str[i:j])
        s.add(hash(inp_str[::-1][i:j].encode('utf-8')))
        s1.add(inp_str[::-1][i:j])

print(s)
print(s1)
