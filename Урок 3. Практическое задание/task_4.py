"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import uuid
import hashlib
import requests


class WebCache:

    def __init__(self, salt):
        self.__salt = salt
        self.__cached_pages = dict()

    def __get_hash(self, argstr):
        argstr_and_salt = self.__salt.encode("utf-8") + argstr.encode("utf-8")
        str_hash = hashlib.sha256(argstr_and_salt)
        str_hash_hex = str_hash.hexdigest()
        return str_hash_hex

    def get_url(self, url):
        url_hash = self.__get_hash(url)
        if self.__cached_pages.get(url_hash):
            print("Нашел в кэше")
            return self.__cached_pages[url_hash]
        else:
            print("Закешировал")
            response = requests.get(url)
            self.__cached_pages[url_hash] = response

        return self.__cached_pages[url_hash]


def get_data(web_cache, url):
    data = web_cache.get_url(url)
    print(f"Первые 10 символов {data.content[0:10]}")


def main():
    pass
    try:
        salt = uuid.uuid4().hex
        web_cache = WebCache(salt)
        url_list = ["https://ya.ru/", "https://github.com/login", "https://ya.ru/"]
        for url in url_list:
            get_data(web_cache, url)

        print("\nПрограмма завершена!")

    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
