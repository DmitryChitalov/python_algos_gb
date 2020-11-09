"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib

mac_address = '08EDB949B2E5'  # соль
history = {}
url_list_1 = ['https://ru.wikipedia.org/', 'https://habr.com/ru/', 'https://ru.stackoverflow.com/']
url_list_2 = ['https://ru.wikipedia.org/', 'https://habr.com/ru/', 'https://ru.stackoverflow.com/',
              'https://pythonru.com/', 'https://yandex.ru/', 'https://mail.ru/', 'https://issue.life/',
              'https://habr.com/ru/']


def visited_url(url_list):
    i = 0
    for url in url_list:
        url_hash = hashlib.sha256(mac_address.encode() + url.encode()).hexdigest()
        record = history.get(url_hash)
        if record is None:
            history[url_hash] = url
            i += 1

    return f'В историю добавлено {i} записи, всего {len(history)} записей'


print(visited_url(url_list_1))

print(visited_url(url_list_2))
