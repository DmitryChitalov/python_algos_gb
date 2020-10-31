"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
import time


def history_browse(url):
    salt = str(int(time.time() // 86400))  # соль меняется 1/сутки
    # (страницы со сроком более суток будут заново добавлятся в кэш)
    url_hash = hashlib.sha256(url.encode()).hexdigest() + ':' + salt
    if url_hash not in history.values():
        history.update({time.time(): url_hash})
        return f'URL {url} добавлена в историю'
    else:
        return f'ссылка {url} уже есть в истории'


history = dict()
while True:
    link = input('Скопируйте сюда URL (или введите "exit"): ')
    if link == 'exit':
        break
    print(history_browse(link))
