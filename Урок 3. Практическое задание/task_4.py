"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import md5

salt = b'root'
storage = {}

def cache_page(url):
    if storage.get(url):
        print(f'Страница с адресом "{url}" уже есть в кэше')
    else:
        storage[url] = md5(salt + url.encode()).hexdigest()
        print(storage)


cache_page('yandex.ru')
cache_page('google.com')
cache_page('yandex.ru')
