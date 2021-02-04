"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import requests
import uuid
import hashlib


def get_hash(url):
    # salt = uuid.uuid4().hex
    salt = "1a988d54f5294a93937a3beac4e16e69"
    # print(salt)
    hash_str = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    res = ""
    for i in hash_str:
        if i.isdigit():
            res += i
    return int(res[7] + res[19])


class PageCacheHashTable:
    size = 100

    def __init__(self):
        self._data = [None] * self.size

    def __getitem__(self, key):
        h = get_hash(key)
        return self._data[h]

    def __setitem__(self, key, value):
        h = get_hash(key)
        self._data[h] = value

    def Contains(self, url):
        index = get_hash(url)
        return self._data[index] is not None


def get_page_from_server(url):
    print("Забираем статью с сервера...")
    response = requests.get(url)
    return response.text


def get_page(url):
    print("Получаем статью...")

    if not cache.Contains(url):
        print("пробуем поместить в кеш.")
        cache[url] = get_page_from_server(url)
        print("Поместили в кеш.")
    else:
        print("страница "+url+" уже в кеше")
    return cache[url]


if __name__ == '__main__':
    url1 = "https://mail.ru/"
    url2 = "https://yandex.ru/"
    # cache = dict()
    cache = PageCacheHashTable()
    get_page(url1)
    get_page(url2)
    get_page(url1)
    get_page(url2)
    # print(get_page(link))
    # print(cache)
    # print(get_page_from_server(link))
    # print(uuid.uuid4().hex)

    # print("!!!! " + str(get_hash(url1)))
    #print(cache[url1])
