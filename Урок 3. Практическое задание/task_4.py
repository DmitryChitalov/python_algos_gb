"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import hashlib
import urllib.request

class UrlCasher():
    def __init__(self):
        """ Инициализирует структуры для хранения страниц"""
        #self.current_url = ''
        self.cashed_url = dict()
        return

    def check_url(self, url_link):
        """ Проверяет есть ли данная ссылка в кэше"""

        hash_url = hashlib.sha256(url_link.encode('utf-8')).hexdigest()
        if self.cashed_url.get(hash_url) != None:
            return print("Данная страница уже есть в кэше")
        else:
            print('Страницы нет в кэше. Кешируем')
            self.cash_url(url_link)
        return

    def cash_url(self, url_link):
        """ Кэшируем веб-страницу"""
        req = urllib.request.urlopen(url_link) # открываем страницу
        content = req.read() # считываем в виде байтов содержимое страницы

        hash_url = hashlib.sha256(url_link.encode('utf-8')).hexdigest() # делаем хеш ссылки
        hash_content = hashlib.sha256(content).hexdigest() # делаем хеш контента

        self.cashed_url[hash_url] = hash_content+ ':'+ hash_url # солим хеш контента

        return

    def get_hash_content(self, url_link):
        """ Возвращает дайджест кешированной страницы"""

        hash_url = hashlib.sha256(url_link.encode('utf-8')).hexdigest()

        if self.cashed_url.get(hash_url) != None:
            return print(f"Дайджест страницы: {url_link} \n", self.cashed_url[hash_url])
        else:
            print('Страницы нет в кэше. Кешируем')
            self.cash_url(url_link)
        return


# клиентская часть

if __name__ == '__main__':
    casher = UrlCasher()

    casher.check_url('https://www.yandex.ru')
    casher.check_url('https://www.google.com')

    casher.check_url('https://www.yandex.ru')
    casher.get_hash_content('https://www.yandex.ru')

