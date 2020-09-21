"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

d_cache = {}


def cashe_func(url, salt='salt'):
    cashe_url = hashlib.sha256((url).encode()).hexdigest() + hashlib.sha256(salt.encode()).hexdigest()
    if url not in d_cache.keys():
        d_cache[hashlib.sha256((url).encode()).hexdigest()] = cashe_url
        return d_cache


if __name__ == '__main__':
    url = 'mail.ru'
    url1 = 'yandex.ru'
    url2 = 'mail.ru'
    url3 = 'google.com'
    print(cashe_func(url))
    print(cashe_func(url1))
    print(cashe_func(url2))
    print(cashe_func(url3))