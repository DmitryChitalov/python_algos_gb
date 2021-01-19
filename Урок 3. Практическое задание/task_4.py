"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


class WebCache:
    def __init__(self):
        self.cache = {}

    def add_web_cache(self, url):
        salt = hash(url)
        hash_obj = hashlib.new('sha512')
        hash_obj.update((url + str(salt)).encode('utf-8'))
        if hash_obj.hexdigest() not in self.cache.keys():
            self.cache.update({hash_obj.hexdigest(): url})

    def print_cache_table(self):
        for cas, elem in self.cache.items():
            print(f'{cas} - {elem}')


if __name__ == '__main__':
    web = WebCache()
    web.add_web_cache('https://www.google.com/')
    web.add_web_cache('https://yandex.ru/')
    web.add_web_cache('https://www.google.com/')
    web.add_web_cache('https://yandex.ru/')
    web.add_web_cache('https://www.python.org/')
    web.print_cache_table()



