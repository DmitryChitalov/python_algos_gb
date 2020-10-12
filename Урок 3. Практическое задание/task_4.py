"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import requests
import hashlib

def hash_creator(line):
    return hashlib.sha256(bytes(line.encode(encoding='UTF-8')) + bytes((str(pow(len(line), 2))*len(line)).encode(encoding='UTF=8'))).hexdigest()


def url_hash_checker(url, cash_tab: dict):
    headers = {'user-agent': 'my-app/0.0.1'}
    if hash_creator(url) not in cash_tab:
        page = requests.get(url, headers)
        print(page)
        cash_tab[hash_creator(f'{url}')] = hash_creator(page.text)
        return cash_tab
    else:
        print('Already exist')
        return cash_tab

url_list = ['https://ya.ru', 'https://api.github.com/events', 'https://ya.ru']
cash = {}

for obj in url_list:
    cash = url_hash_checker(obj, cash)

print(cash)
