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
# одредактировал по примеру
import hashlib


string = input("Enter some string: ")
r = set()

N = len(string)

for i in range(N):
	if i == 0:
		N = len(string) - 1
	else:
		N = len(string)
	for j in range(N, i, -1):
		print(string[i:j])

		r.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
print(r)
