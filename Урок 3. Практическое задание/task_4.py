"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


class WebCash:

    def __init__(self):
        self.urls = {}

    def get_content(self, url):
        if self.urls.get(url):
            print('В кэше есть данный url: {}'.format(self.urls.get(url).decode()))
        else:
            salt = uuid4().hex
            hash_url = hash_the_object(url)
            self.urls[url] = hash_url
            print('В кэше нет данного url')

