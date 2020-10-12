"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""


import hashlib, uuid, time, requests


class ContentCaching:
    
    def __init__(self, cache_life=30):
        self.__cache = dict()
        self.__cache_life = int(cache_life)
        self.__salt = uuid.uuid4().hex

    def __check_cache(self, url_hash):
        """Метод проверки наличия данных в кэше и их годность

        :param url_hash: захешированный URL
        :return: Возвращает контент если есть, либо None
        """
        cache = self.__cache.get(url_hash)
        if cache is not None and cache['timeout'] > time.time():
            print(f"\n **** Content found in cache (time left: {cache['timeout'] - int(time.time())}) **** \n")
            return cache['content']
        else:
            return None

    def __set_cache(self, url, content):
        """Метод записи контента страницы в кэш

        :param url: URL адрес страницы
        :param content: Контент страницы (HTML-код)
        """
        url_hash = self.__url_hash(url)
        self.__cache[url_hash] = {
            'timeout': int(time.time()) + self.__cache_life,
            'url': url,
            'content': content
        }
        print('\n **** Content added to cache **** \n')

    def status_cache(self):
        """Метод вывода статуса кэша

        :return: Выводит в терминал состояние кэша
        """
        print(f"\n{'- ' * 30}\nСтатус кэша:\n * Всего в кэше: {len(self.__cache)}")
        for i, cache in enumerate(self.__cache):
            row = f"\t{i}: "
            row += f"hash: {cache}, "
            row += f"time left: {int(self.__cache[cache]['timeout'] - time.time()) if self.__cache[cache]['timeout'] > time.time() else 'протухло'}, "
            row += f"url: {self.__cache[cache]['url']}, "
            row += f"длина контента: {len(self.__cache[cache]['content'])}"
            print(row)
        print('- ' * 30, end="\n\n")

    def __url_hash(self, url):
        """Метод хеширует URL-адрес

        :param url: URL адрес страницы
        :return: Возвращает захешированный URL страницы
        """
        return hashlib.md5(self.__salt.encode() + url.encode()).hexdigest()
    
    def get_content(self, url):
        """Метод получения контента страницы

        :param url: URL адрес страницы
        :return: Возвращает контент страницы (HTML-код)
        """
        if url.find('http://') != 0 and url.find('https://') != 0:
            url = 'http://' + url
            print(url)
        url_hash = self.__url_hash(url)
        content = self.__check_cache(url_hash)
        if content is not None:
            return content
        else:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    self.__set_cache(url, r.text)
                else:
                    print(f"Код ответа: {r.status_code}")
                return r.text
            except:
                print('Адрес не найден!')
                return ''


#################################
cc = ContentCaching()

while True:
    url = input("Введите URL сайта (для выхода просто нажмите Enter): ")
    if url == '':
        break
    site_content = cc.get_content(url)
    print(f"Длина тела ответа: {len(site_content)}")
    cc.status_cache()

print('\nВыход\n')
