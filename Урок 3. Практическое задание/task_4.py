"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from hashlib import sha256

url_hash_dict = {'https://vk.com/': '3f44b1e12fff310d122c3af3504b4f18b27a008e8f9280f5e45911a9e45a0e3c'}


class CachedLink:
    def __init__(self, url_input):
        self.url_input = url_input
        self.salt = self.url_input[::-1].encode("utf-8")  # солью выступает перевёрнутый наоборот URL-адрес

    def __make_hash(self):
        return sha256(self.salt + self.url_input.encode('utf-8')).hexdigest()

    def check_link(self):
        if url_hash_dict.get(self.url_input) is None:
            url_hash_dict[self.url_input] = self.__make_hash()
            print('Адрес кеширован.')
        else:
            print('Адрес присутствует в таблице кеширования.')


try:
    url_input = input('Введите URL-адрес: ')
    if 'http' not in url_input[:4]:  # проверка на формат ввода URL-адреса
        raise ValueError('Ошибка формата ввода URL-адреса.')
    CachedLink(url_input).check_link()
except ValueError:
    print('Ошибка формата ввода URL-адреса.')
