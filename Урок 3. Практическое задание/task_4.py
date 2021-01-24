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

salt = uuid4().hex
obj = {}


def page_check(site):
    if obj.get(site):
        print(f'Адрес {site} - в кэше.')
    else:
        print(f'Адреса {site} нет в кэше')
        obj[site] = hashlib.sha256(salt.encode() + site.encode()).hexdigest()


page_check("https://yandex.ru")
page_check("https://yandex.ru")
