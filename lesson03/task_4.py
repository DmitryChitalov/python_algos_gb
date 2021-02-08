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


def memorize(func):
    def g(arg, memory={}):
        r = memory.get(arg)
        if r is None:
            r = func(arg)
            memory[arg] = r
        return r

    return g


@memorize
def hash_url(url):
    salt = "any_salt"
    hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    return hashed_url
