"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


def add_to_url(url, salt, dict):
    if url not in hash_dict.keys():
        salted_url = hashlib.sha256(salt.encode('utf-8') + url.encode('utf-8')).hexdigest()
        dict[url] = f'{salted_url}'


hash_dict = {}

while input('Добавляем сайт? д/н ') == 'д':
    site = input('Write any url: ')
    add_to_url(site, 'hello kitty', hash_dict)

print(hash_dict)
