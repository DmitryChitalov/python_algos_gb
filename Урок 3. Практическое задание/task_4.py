"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


def memorize(func):
    def wrapper(result, memory={}):
        cache = memory.get(result)
        if cache is None:
            cache = func(result)
            memory[result] = cache
            print(memory)
        return cache
    return wrapper


@memorize
def cache_url(url):
    salt = 'any_salt'
    result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    return result


cache_url('https://geekbrains.ru/lessons/84942')