"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


def check_url():
	a = []
	while True:
		url = input('Enter url or q for exit: ')
		if url == 'q':
			print('Finish programm\n')
			return 
		else:
			h = hashlib.sha256(url.encode('utf-8')).hexdigest()
			if h in a:
				print('Web site open\n')
			else:
				a.append(h)
				print("Web site added to chache\n")
				
				
check_url()
