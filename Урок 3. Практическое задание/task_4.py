"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import md5

salt = b'maxsar'
storage = {}

def cache_page(url):
    if storage.get(url):
        print(f'Страница с адресом "{url}" уже есть в кэше')
    else:
        storage[url] = md5(salt + url.encode()).hexdigest()
        print(storage)


cache_page('google.ru')
cache_page('vk.com')
cache_page('yandex.ru')