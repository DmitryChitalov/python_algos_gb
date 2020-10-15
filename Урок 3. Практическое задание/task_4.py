"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib

salt = 'Hello'
cache_page = {}


def get_page(url):

	if cache_page.get(url):
		print("Cache is available")
	else:
		res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
		cache_page[url] = res
		print(cache_page)


get_page('https://google.com')
get_page('https://google.com')

