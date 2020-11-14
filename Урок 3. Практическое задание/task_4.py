"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


class CacheURL:
    def __init__(self, salt:str):
        self.__salt = salt
        self.memory = set()

    def hash_url(self, new_url:str):
        return hashlib.sha256(self.__salt.encode() + new_url.encode()).hexdigest()

    def check_url(self, new_url:str):
        return self.hash_url(new_url) in self.memory

    def add_url(self, new_url:str):
        if self.check_url(new_url):
            print(f'веб-страница "{new_url}" уже имеется в памяти')
        else:
            self.memory.add(self.hash_url(new_url))
            print(f'Веб-страница "{new_url}" добавлена в кеш')

    def del_url(self, del_url:str):
        self.memory.discard(del_url)
        print(f'Веб-страница удалена и кеша')


if __name__ == '__main__':
    my_browser = CacheURL('Hello World')
    my_browser.add_url('https://vk.com/feed')
    my_browser.add_url('https://vk.com/')
    my_browser.add_url('https://vk.com/friends')
    my_browser.add_url('https://vk.com/albums')
    my_browser.add_url('https://vk.com/video')
    my_browser.add_url('https://vk.com/apps')
    print(len(my_browser.memory))
    print(my_browser.memory)