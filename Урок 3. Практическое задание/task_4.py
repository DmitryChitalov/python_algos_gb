"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""
from uuid import uuid4
import hashlib


class Browser:
    def __init__(self):
        self.cach = dict()
        self.salt = uuid4().hex  # соль для текущего объекта

    def get(self, url):
        url_hash = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()  # Хеш с солью для адреса
        page = self.cach.get(url_hash)
        if page:
            print('объект из кэша')
            return page
        else:
            page = str(uuid4())  # симулируем получение страницы
            self.cach.update({url_hash: page})  # в уроке было задание хранить в словаре {url_hash: url}, чуть усложнил
            print('объекта не было в кэше')
            return page


if __name__ == '__main__':
    b = Browser()
    while True:
        my_url = input('Введите адрес:  ')
        print(b.get(my_url))
