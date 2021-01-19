"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['gbscrapy']
collection = db['my_url']


def hash_url(url):
    res = hashlib.md5(url.encode('utf-8')).hexdigest()
    item = collection.find_one({"hash": res})
    if item is None:
        collection.insert_one({"hash": res, 'url': url})
        return print("Адрес добавлен в базу")
    else:
        print("Такой адрес есть")
        return item["url"]


print(hash_url(input("Введите адрес сайта: ")))
