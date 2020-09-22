"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
##################################################################################################
"""
Программа работает)))
При получении url адреса программа проверяет его наличие в словаре. Если его там нет, 
добавляет в словарь ключ хеш. А также запись в таблицу данных. Если есть берет запись из БД.
Мне кажеться это избыточным. Достаточно проиндексировать в бд столбец с хешами. Но в данном вопросе
не хватает знаний и надо разбираться дальше.
"""

import hashlib
import dataset
import requests
from bs4 import BeautifulSoup

name_data_base = "dz_3"  # имя бд
name_table = 'web_page'

name_db = f'sqlite:///{name_data_base}.sqlite3'

db = dataset.connect(name_db)
table = db[name_table]


def get_page(link_p):
    """
    функция исправляет url адрес
    :param link_p: str
    :return: str
    """
    if link_p[0:4] == 'http':
        url_web = link_p
    else:
        url_web = f'http://karelohota.ru/{link_p}'
    return url_web


def get_next_pages(page):
    """функция нужна для поиска ссылки на следующию страницу"""
    try:
        soup = BeautifulSoup(page, "lxml")
        link_list = []
        for link in soup.find_all('a'):
            link_list.append(link['href'])
        return link_list
    except Exception as err:
        print(err)
        return False


def get_page_from_web(url_web_in):
    """
    функция получает страницу из интернета по адресу
    :param dist_control:
    :param url_web: str
    :return:
    """
    r = requests.get(url_web_in)
    print(r.status_code)
    return r.text


def create_hash(ur):
    salt = 'I am salt, but I do not know, why I am here'
    a = hashlib.sha3_256(ur.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    print(a)
    return a


def check_page(hash_url, dict_control):
    if dict_control.get(hash_url):
        return True
    else:
        return False


def main(link_to_page, dist_control={}, list_link=[], _counter=-1):
    url_web = get_page(link_to_page)
    hash_adress = create_hash(url_web)
    if check_page(hash_adress, dist_control):
        content = table.find_one(key=hash_adress)
        print(type(content))
    else:
        page_obj = get_page_from_web(url_web)
        dist_control[hash_adress] = True
        table.insert(dict(key=hash_adress, url=url_web, value=page_obj))
        link_from_page = get_next_pages(page_obj)
        if link_from_page is not False:
            list_link.extend(get_next_pages(page_obj))
    _counter += 1
    print(list_link[_counter])
    if _counter == 100:
        return
    main(list_link[_counter], dist_control, list_link, _counter)


if __name__ == '__main__':
    main('http://karelohota.ru/index.html')
    print("-----" * 5)

