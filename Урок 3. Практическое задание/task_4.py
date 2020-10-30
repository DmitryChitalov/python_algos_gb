"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib

oDictFrom = {'url1':'data1',
             'url2':'data2',
             'url3':'data3',
             'url4':'data4',
             'url5':'data5',
             'url6':'data6'}

oDictTo = {}

def add_to_cache():
    url = input('url (0 - выход): ')
    if url == '0':
        return
    if validation(url):
        print('url нет в кэш, делаем хеширование')
        data = data_to_hash(url)
        print('солёный хеш готов')
        oDictTo[url] = data.hexdigest()
        print('добавили')
    else:
        print('такой уже есть, или введён не верный')
        add_to_cache()

def data_to_hash(url):
    b_salt = bytes(url, 'utf-8')
    print('солим url\'ом')
    return hashlib.sha256(bytes(oDictFrom[url], 'utf-8') + b_salt)


def validation(url):
    if url not in oDictTo and url in oDictFrom:
        return True


add_to_cache()

