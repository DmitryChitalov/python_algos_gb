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

# user_url = input("Введите url-адрес страницы: ").encode('utf-8')
sal = uuid4().hex
cash_list = {}


def check_url(url):
    if cash_list.get(url):
        print(f'Cтраница {url} уже в кеше есть ')
    else:
        hash_url = hashlib.sha256(sal.encode() + url.encode()).hexdigest()
        cash_list[url] = hash_url
        print(f'Cтраница {url} добавлена в кеш ')
        # print(cash_list)


while True:
    user_url = input("Введите url-адрес страницы: ")
    check_url(user_url)
    if user_url == '':
        break

