"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

salt = 'salt'

url_list = set()


def url_filler(url):
    global url_list

    hashed_url = hashlib.sha1(url.encode() + salt.encode()).hexdigest()
    print(hashed_url)
    if hashed_url in url_list:
        print('URL уже есть в списке')
    else:
        print('добавляем новый URL во множество')
        url_list.add(hashed_url)


url_filler('www.mywebsite.com/page1')
url_filler('www.mywebsite.com/page1')
url_filler('www.mywebsite.com/page1/topic1')
url_filler('www.mywebsite.com/page1/topic1')
