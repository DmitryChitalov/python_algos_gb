"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
import hashlib


def save_url(test_url, url_dict={}):
    salt = b'url'
    if hashlib.sha256(test_url.encode() + salt).hexdigest() not in url_dict.values():
        url_dict[test_url] = hashlib.sha256(test_url.encode() + salt).hexdigest()
        print('Страница внесена в хэш')
    else:
        print('Страница уже в хэше')


dict1 = {}
save_url('dgfhdj')
save_url('dgfhdj')
print('******')

''' ************************************************'''

class Web_save_to_hash():
    def __init__(self):
        self.dict_url = {}
        self.salt = b'salt'

    def add_url(self, url_add):
        if hashlib.sha256(url_add.encode() + self.salt).hexdigest() not in self.dict_url.values():
            self.dict_url[url_add] = hashlib.sha256(url_add.encode() + self.salt).hexdigest()

    def print_dict(self, test_web_url):
        """ Функция для собственной поверки """
        if hashlib.sha256(test_web_url.encode() + self.salt).hexdigest() in self.dict_url.values():
            print("OK", self.dict_url[test_web_url])
        else:
            print("NO")


c = Web_save_to_hash()
c.add_url('web@dh')
c.print_dict('web@dh__1')
c.print_dict('web@dh')
