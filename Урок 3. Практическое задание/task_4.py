"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import pbkdf2_hmac
from binascii import hexlify

cash_url = {}


def get_hash(v):
    s = str(v.split('.')[:-1]).encode()
    return pbkdf2_hmac(hash_name='sha256',
                       password=v.encode(),
                       salt=s,
                       iterations=10000)


def check_url(v_url):
    if cash_url.get(hexlify(get_hash(v_url))):
        print(f'This page already {v_url} exist in cache')
    else:
        cash_url.update({hexlify(get_hash(v_url)): v_url})
        print(f'Put in cache {v_url}')