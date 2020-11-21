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

def url_to_hash(url):
    curr_cash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    # url = input('Введите адрес url страницы: ')
    try:
        url_cash.index(curr_cash)
        print(f'Данный url: {url} находится в кэш')
    except ValueError:
        url_cash.append(curr_cash)
        print(f'Данный url: {url} добавлен в кэш')


salt = uuid4().hex
url_cash = []

url_to_hash('https://mail.ru/')
url_to_hash('https://yaplakal.com/')
url_to_hash('https://picabu.ru/')
url_to_hash('https://vk.com.ru/')
url_to_hash('https://picabu.ru/')
url_to_hash('https://picabu.ru/')
url_to_hash('https://picabu.ru/')
