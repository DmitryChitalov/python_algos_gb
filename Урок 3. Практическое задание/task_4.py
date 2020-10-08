"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import requests
from hashlib import pbkdf2_hmac
from binascii import hexlify


def site_req(user_site):
    salt = 'Введите пароль:'
    url = 'http://' + user_site
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
        'cache-control': 'private, max-age=0, no-cache'
    }
    print(url)
    resp = requests.get(url, headers=headers).text
    obj = pbkdf2_hmac(hash_name='sha256',
                      password=resp.encode('utf-8'),
                      salt=salt.encode('utf-8'),
                      iterations=100000)
    return obj


site_list = []
site = input('Введите адрес сайта:')
while site != '0':
    if site != '0':
        url_h = hexlify(site_req(site))
        if url_h in site_list:
            print('сайт уже кэширован')
        else:
            site_list.append(url_h)
        site = input('Введите адрес сайта:')
    else:
        break
print(site_list)
