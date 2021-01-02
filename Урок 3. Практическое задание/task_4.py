"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib

# Не очень поняла это задание, попробую сделать, как поняла...
# В частности, не совсем поняла, как создавать кеш-таблицу, о которой рассказывали на уроке и откуда брать для нее ключи...
# Как поняла, словарь в Python это и есть кэш, котроый имеется ввиду в задании, а судя по примеру "Листинг 9. task_9.py",
# ключи не генерятся, а ключами будут сами адреса переданных страниц...

url_cash = {}
salt = 'sh9tothestars'


def url_find_cash(url_address):
    if url_cash.get(url_address) == None:
        url_cash[url_address] = hashlib.sha256(salt.encode() + url_address.encode()).hexdigest()
    else:
        print('Страница найдена! Ее хэш: ', url_cash.get(url_address))


url_find_cash('https://vk.com/')
print(url_cash)
url_find_cash('https://www.google.com/')
print(url_cash)
url_find_cash('https://github.com/')
print(url_cash)
url_find_cash('https://www.google.com/')
print(url_cash)
