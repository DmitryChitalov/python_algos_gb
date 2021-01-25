"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib

cache_lst = []
def cache(url_adress='geekbrains.ru', salt='name'):
    url_adress = hashlib.sha256(url_adress.encode() + salt.encode())
    url_adress = url_adress.hexdigest()
    if url_adress not in cache_lst:
        cache_lst.append(url_adress)
        print('added')
        return

url_input = input('url adress ')
salt = input('salt ')
while url_input and salt:
    cache(url_input, salt)
    url_input = input('url adress ')
    salt = input('salt ')
print(cache_lst)

