"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib

a = 'www.google.com'
b = 'www.ya.ru'
c = 'vk.com'
d = 'https://qwerty.eu/hello'


class Url_Cash:
    def __init__(self):
        self.cash = {}

    def hash_url(self, url):
        if url[0:3] == 'www':  # Добавить соль по домену
            salt = url[url.find('.') + 1:url.find('.', 4)]
        elif url[0:8] == 'https://':
            salt = url[url.find('//') + 2:url.find('.')]
        else:
            salt = url[:url.find('.')]
        data = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        if salt in self.cash:
            print('Адрес уже находится в кэше')
            return
        else:
            print('Адрес добавлен в кэш')
            self.cash[salt] = data
        return

my_cash = Url_Cash()
my_cash.hash_url(a)
my_cash.hash_url(a)
my_cash.hash_url(b)
my_cash.hash_url(b)
my_cash.hash_url(c)
my_cash.hash_url(c)
my_cash.hash_url(d)
my_cash.hash_url(d)
my_cash.hash_url(input('Введите адрес: '))
print(my_cash.cash)