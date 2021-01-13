"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
import hashlib


def my_second_decorator(my_func):
    def wrapper(url_dict={}):
        url = input("Введите url: ")
        r = url_dict.get(url)
        if r is None:
            salt = uuid4().hex
            hash_obj = my_func(url, salt)
            url_dict[url] = hash_obj
            return url_dict
        else:
            return f"{url} уже в кэше"
    return wrapper

@my_second_decorator
def take_url(some_url, some_salt):
    hash_obj = hashlib.sha256(some_salt.encode("utf-8") + some_url.encode("utf-8"))
    return hash_obj.hexdigest()


while True:
    x = take_url()
    print(x)
    exit_from_loop = input("Для выхода введите 1, для продолжения все остальное: ")
    if exit_from_loop == '1':
        break
