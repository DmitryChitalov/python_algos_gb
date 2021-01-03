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
# Накостылил как смог, зато без гула
import hashlib

string = input("Введите строку: ")
long = len(string)
setter = set()
setter2 = set()

for elem in range(long):
    if elem == 0:
        string = string[::-1]
        for elem in range(long):
            setter.add(string[0:elem])
    else:
        string = string[::-1]
        setter.add(string[0:elem])
for el in setter:
    setter2.add(el)
    setter2.add(el[::-1])

setter = setter.union(setter2)
setter.remove('')

setter2.clear()
for elem in setter:
    setter2.add(hashlib.sha1(elem.encode('utf-8')).hexdigest())

print(setter2)
