"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha256

url_cache = [
    'da6cca7493411a39695c654313a7d7e51092ef8633ca7cbf81d9a606cd43d610',
    'ce5ce0e5a83da4978e6a3035bd96128bcff8d5845a77abe27b859d0fee42f963'
]  # 'yandex.ru', 'mail.ru'


def url_hash(url):
    salt = url
    new_hash_url = sha256(url.encode() + salt.encode()).hexdigest()
    if new_hash_url in url_cache:
        return f'Адрес "{url}" уже есть в кэше'
    else:
        url_cache.append(new_hash_url)
        return f'Адрес "{url}" добавлен в кэш'


print(url_cache)  # изначальное сосотояние кэша
print(url_hash('yandex.ru'))  # -> Адрес "yandex.ru" уже есть в кэше
print(url_cache)  # кэш не изменился
print(url_hash('google.com'))  # -> Адрес "google.com" добавлен в кэш
print(url_cache)  # кэш изменился
