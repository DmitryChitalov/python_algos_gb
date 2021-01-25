"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib
import string
import random

cache = {}


def generate_salt(length):
    '''
    Функция генерации соли
    :param length: не меньше 16 символов для большей безопасности
    :return: Возвращается строка mix
    '''
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def cache_site(site):
    if cache.get(site):
        print(f'Адрес {site} - в кэше.')
    else:
        print(f'Адреса {site} нет в кэше')
        salt = generate_salt(16)
        cache[site] = hashlib.sha256(salt.encode() + site.encode()).hexdigest()


cache_site("https://google.com")
cache_site("https://google.com")
cache_site("https://yahoo.com")
cache_site("https://amazon.com")
cache_site("https://amazon.com")