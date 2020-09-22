"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
import urllib.parse as up

cache = {}

text = ['https://pythonworld.ru/osnovy/dekoratory.html',
        'https://pythonworld.ru/osnovy/dekoratory.html',
        'https://pythonworld2.ru/osnovy/dekoratory.html',
        'https://pythonworld2.ru/osnovy/dekoratory.html',
        'https://pythonworld2.ru/osnovy3:/dekoratory.html',
        'https://yandex.ru/osnovy3:/dekoratory.html']


def add_cache(url):
    # вытаскиваем адресс сайта
    netloc = up.urlparse(url).netloc
    # вытаскиваем адресс страницы сайта
    path = up.urlparse(url).path
    # создаем "соленый" хеш
    hash_string = hashlib.sha256(netloc.encode() + path.encode()).hexdigest()
    if netloc not in cache:
        cache[netloc] = []
        cache[netloc].append(hash_string)
    else:
        if hash_string not in cache[netloc]:
            cache[netloc].append(hash_string)


for i in text:
    add_cache(i)

print(cache)
