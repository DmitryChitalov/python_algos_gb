"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256


def hash_page(url, hash_lib={}):
    salt = 'Cayman'
    if url in hash_lib.keys():
        print(f'Страница с адресом {url} уже присутствует в кэше')
        return hash_lib[url]
    else:
        hash_lib[url] = sha256(url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        print(f'Страница с адресом {url} внесена в кэш')
        return hash_lib[url]


print(hash_page('http://nuancesprog.ru'))
print(hash_page('http://soccer.ru'))
print(hash_page('http://F1-world.ru'))
print(hash_page('http://nuancesprog.ru'))
