"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib

cache_pages={}


def ch_url(url):
    salt = 'All you need is love'
    if url in cache_pages:
        print('This URL is already in.')
    else:
        hash_salt_url= hashlib.sha256(url.encode()+salt.encode()).hexdigest()
        cache_pages.update({url:hash_salt_url})
        print(cache_pages)

ch_url('https://docs.python.org/3.9/whatsnew/3.9.htm');
ch_url('https://docs.python.org/3.9/whatsnew/3.9.htm');


