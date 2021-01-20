"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha256


class UrlStorage:
    def __init__(self):
        self.url_dict = dict()

    def add_url(self):
        while True:
            user_url = input('Введите url:\n')
            if user_url == 'stop':
                print('Ввод окончен')
                break
            elif user_url not in self.url_dict.keys():
                salt = input('Введите логин:\n')
                self.url_dict[user_url] = sha256(user_url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
                print('Сайт добавлен')
            else:
                print('Сайт уже есть в списке')

    def __str__(self):
        return 'Добваленные адреса:\n' + '\n'.join(self.url_dict.keys())


test = UrlStorage()
test.add_url()
print(test)