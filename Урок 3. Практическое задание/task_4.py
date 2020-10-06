"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

my_dict = {'vk.com/': 'a0f7c8fab228266ef5228ab96cf4a8dfcd60e6093b5ee2d5c71759b1cc37ad61:vk.com/',
           'geekbrains.ru/': '21498adf1be23e159a98295f467b99b72c4b67f7ac22627d517905f5de4cfbb8:geekbrains.ru/',
           'pythonworld.ru/': '65fa233d94ab5ec50373d70d1d9d5e7e39eed50b621d199afc926866a5759356:pythonworld.ru/'
           }


def check_my_dict(s_dict):
    url = input('enter ur url: ')
    if url in s_dict:
        return print('true')
    else:
        salt = url
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
        print(res)
        s_dict[url] = res
    return print(s_dict)


check_my_dict(my_dict)
