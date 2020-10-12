"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

salt = 'hello url'
my_hash_url_list = []

def url():
    while True:
        check_url = input('Введите url-адресс (для выхода, введите q) ')
        if check_url == 'q':
            print(my_hash_url_list)
            break
        check_url = hashlib.sha256(check_url.encode()).hexdigest()
        if check_url in my_hash_url_list:
            print('Такой url уже внесен')
        else:
            my_hash_url_list.append(check_url)
            print('url внесен в список')

url()