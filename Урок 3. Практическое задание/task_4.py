"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
(Чтобы не хранить страницы в виде url, а в виде хешей)
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП

"""
# импорт создание случайного уникального индификатора UUID
# импорт hashlib хэш-библиотеки Python для хеширования строк
from uuid import uuid4
import hashlib

salt = uuid4().hex  # -> 952604f24d9f4cd0b515a39c73657027 (соль)
cache_obj = {} # фарш таблица


def get_page(url): # функция кеширующая url-ы
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('https://geekbrains.ru/')
get_page('https://google.com/')
get_page('https://mail.ru/')
get_page('https://geekbrains.ru/')
