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

def check_string():
	string = input('Введите строку:')
	count = 0
	a = set()
	for i in range(len(string) - 1):
		for j in range(i+1, len(string) + 1):
			if len(string[i:j]) < len(string):
				print(string[i:j])
				a.add(hashlib.sha256(string[i:j].encode('utf-8')).hexdigest())
				count += 1
	print(f'Из {count} сочетаний, уникальных {len(a)}')
	return a

a = check_string()

