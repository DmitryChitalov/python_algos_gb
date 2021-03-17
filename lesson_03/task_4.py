"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


import hashlib


class Cash:

    def __init__(self):
        self.cash = dict()

    @staticmethod
    def hash_url(url):
        salt = url[-5:]
        url_hash = hashlib.sha256(url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        return url_hash

    def add_to_cash(self, url):
        url_hash = self.hash_url(url)
        if url_hash not in self.cash:
            self.cash[url_hash] = url
            print(f'url {url} добавлен в кеш')
        else:
            print(f'url {url} уже имеется в кеше')


if __name__ == '__main__':

    urls_list = [
        'https://geekbrains.ru',
        'https://yandex.ru',
        'https://mail.ru',
        'https://github.com',
        'https://vk.com'
    ]

    test_list = [
        'https://docs.python.org',
        'https://github.com',
        'https://yandex.ru'
    ]

    cash = Cash()
    print('Наполним кеш несколькими url:')
    for item in urls_list:
        cash.add_to_cash(item)
    print('\nВ кеше теперь:')
    for key, value in cash.cash.items():
        print(key, value)

    print('\nТеперь проверим несколько адресов:')
    for item in test_list:
        cash.add_to_cash(item)
    print('\nВ кеше теперь:')
    for key, value in cash.cash.items():
        print(key, value)
