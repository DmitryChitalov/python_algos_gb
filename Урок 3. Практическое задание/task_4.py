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
data_urls = {}
salt = uuid4().hex


def cash_webpages(url):
    res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if len(data_urls) == 0:
        data_urls.update({url: res})
        return "Словарь был пуст, добавлен первый адрес."
    else:
        for items in data_urls.values():
            if items == res:
                return "Адрес уже существует!"
            else:
                data_urls.update({url: res})
                return "Новый адрес добавлен!"


print(cash_webpages(input("Введите адрес страницы: ")))
print(data_urls)




