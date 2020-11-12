"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

def caching_web_pages(wp, cash):
    salt = 'salt'
    res_wp = hashlib.sha256(salt.encode() + (wp).encode()).hexdigest()
    if res_wp in cash.values():
        return f'Страница {wp} уже есть в кэше'
    else:
        cash[wp] = res_wp
        return cash
wp = 'https://geekbrains.ru/'
cash = {'https://intuit.ru/': '8bbd3c9b62d191b0a3170bf8acfa08500038d9af5c12ec40e48076bd70478daa',
        'https://geekbrains.ru/': 'b38e009334a29a3c0fbce7cff86c4d63669f894dcc6fd30f0d06f440a04db864',
        'https://pythonworld.ru/': '47b9b2984d3bd6806ef905c4bae48a21779ef43e9daea4896ffd9132293e8fbe'}
print(caching_web_pages(wp, cash))



