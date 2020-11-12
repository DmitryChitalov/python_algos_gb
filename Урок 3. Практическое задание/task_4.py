"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


def link_to_sha256(lnk):
    salt = lnk + lnk[::-1]
    return hashlib.sha256(lnk.encode() + salt.encode()).hexdigest()


links = {}
k = True
while k:
    link = input('Введите ссылку. Для выхода введите пустую строку: ')
    if link == '':
        for key in links.keys():
            print(f'{key} - {links[key]}')
        k = False
    else:
        if link_to_sha256(link) not in links:
            links[link_to_sha256(link)] = link
        else:
            print('Такая ссылка уже существует в списке.')