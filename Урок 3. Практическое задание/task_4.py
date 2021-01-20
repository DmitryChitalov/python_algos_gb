"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha512
from time import sleep
from random import randint


class MyWebCacheClass:
    def __init__(self):
        self.__cache = []
        self.__salt = 'GeekBrains'.encode('utf-8')

    def open_url(self, url=''):
        if url == '':
            return
        print(f'Открываем страницу {url}...')
        hash_url = sha512(url.encode('utf-8') + self.__salt).hexdigest()
        delay = 'меньше 1'
        if hash_url not in self.__cache:
            delay = randint(1, 5)
            sleep(delay)  # имитация загрузки из интернета))
            self.__cache.append(hash_url)
        print(f'Ok, {delay} сек.')


if __name__ == '__main__':
    web = MyWebCacheClass()
    while True:
        url = input(f'Введите url (для выхода q): ')
        if url == 'q':
            break
        elif url != '':
            web.open_url(url)
