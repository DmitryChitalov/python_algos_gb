"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib


def check_url():
    a = []
    salt = b'coding web pages'
    while True:
        url = input('Enter url or q for exit: ')
        if url == 'q':
            print('Finish program\n')
            return
        else:
            h = hashlib.sha256(url.encode('utf-8') + salt).hexdigest()
            if h in a:
                print('Web site open\n')
            else:
                a.append(h)
                print("Web site added to cache\n")


check_url()
