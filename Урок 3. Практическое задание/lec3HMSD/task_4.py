"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib

link_hash = {}


def check_url(url):
    hashurl = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
    test = link_hash.get(hashurl)
    if link_hash.get(hashurl):
        print("Данная страница уже была ранее Кэширована")
    else:
        link_hash[hashurl] = url
        print("Страница добавлена в Кэш список")


link_hash = {}
salt = "31LD32DSU5dfe"
check_url("ya.ru")
check_url("1c.ru")
check_url("ya.ru")
check_url("my.ru")
check_url("my.ru")

print(link_hash)
