"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
from uuid import uuid4

urls_cache = {}

salt = uuid4().hex


def checking_url(url_obj):
    if urls_cache.get(url_obj):
        return f'Ссылка {url_obj} уже находится в кэше'
    else:
        urls_cache[url_obj] = hashlib.sha256(salt.encode('utf-8') + url_obj.encode('utf-8')).hexdigest()
        print(urls_cache)
        return f'Сылка {url_obj} добавлена в кэш'


if __name__ == '__main__':
    print(salt)
    print(checking_url('https://github.com/Etery89'))
    print(checking_url('http://pythontutor.com'))
    print(checking_url('https://github.com/Etery89'))
