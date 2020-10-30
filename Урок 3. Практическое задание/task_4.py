"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib


def caching_web_pages(url):
    salt = uuid4().hex
    if url not in cache.keys():
        cache[url] = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        return print(f"Такого хэша нет. Страница добавлена.")
    else:
        return print(f"{url} - есть в кеше.")


if __name__ == "__main__":
    cache = {}
    my_url = input("Введите адрес веб-страницы: ")
    caching_web_pages(my_url)
    my_url = input("Введите адрес веб-страницы: ")
    caching_web_pages(my_url)
    print(cache)
