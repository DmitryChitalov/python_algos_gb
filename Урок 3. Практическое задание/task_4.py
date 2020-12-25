"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
# import hashlib
import requests
import mysql.connector
from task_2 import get_hash

#
# def connect_db():
#     conct = mysql.connector.connect(host='localhost',
#                                     database='web',
#                                     user='root',
#                                     password='1234')
#     return conct  # почему-то так не завелось, а сдавать пора, потом починить

def get_data(table):
    conct = mysql.connector.connect(host='localhost',
                                    database='web',
                                    user='root',
                                    password='1234')
    cur = conct.cursor()
    cur.execute(f'select * from {table};')
    data = cur.fetchall()
    return data

def write_data(table,my_url, my_hash):
    conct = mysql.connector.connect(host='localhost',
                                    database='web',
                                    user='root',
                                    password='1234')
    cur = conct.cursor()
    sql = f"insert {table} (url, hash) values (%s, %s)"
    val = (my_url, my_hash)
    cur.execute(sql, val)
    conct.commit()

def get_data_mok(table):
    test=[(1, 'geekbrains.ru', ''), (4, 'https://geekbrains.ru', ''),
          (5, 'https://google.ru', '6bbce80f013a55d6f486c7e47ce80d60a0c3545786b172682b8a2419b6c50bc1'),
          (8, 'https://mail.ru', '1b9057c46bc6d2faef90b5f4e5d4be60e87ed52e1548aadc1f8fd97d0b42b3bd')]
    return test


def get_page(url):
   # r = requests.get(url).text  # если спрашивать весь текст то хеш будет скакать...
   # нужно что-то поменьше и реже меняюшееся. И желательно что есть у всех, нопока пусть так:
   # r = requests.get(url).headers.get('Content-Security-Policy') # в этот момент понимаешь что вобще это была плохая
   # идея реальные страницы опрашивать
   r = requests.get(url).headers.get('server') # ну вот, вебсервер у всех есть, для примера пойдет
   return r

def check_cache(new_url):
    new_digest = get_hash(get_page(new_url), new_url)
    check_list = get_data('hashes')
    counter = 0
    lim = len(check_list)
    for el in check_list:
        counter += 1
        if el[2] == new_digest:
            return 'Такая страница уже есть в кеше'
        elif el[2] != new_digest and el[1]== new_url:
            return 'Кеш записи возможно устарел'
        elif el[2] != new_digest and counter < lim :
            continue
        else:
            # print(new_url, new_digest)
            write_data('hashes', new_url, new_digest)
            return f'Запись для адреса {new_url} успешно закеширована '





if __name__ == '__main__':

    # print(get_data('hashes'))
    # write_data('hashes', 'https://geekbrains.ru', '' )
    # print(get_data('hashes'))
    # print(get_page('https://geekbrains.ru'))
    # print(get_hash(get_page('https://geekbrains.ru'), 'https://geekbrains.ru'))

    # print(get_page('https://geekbrains.ru')) # где-то на 3-м десятке запросов GB  забанил меня по IP))
    test_url='https://google.ru'
    # print(get_page(test_url))
    # print(get_hash(get_page(test_url), test_url))
    # print(check_cache(test_url))
    print(check_cache(test_url))
    test_url = 'https://mail.ru'
    print(check_cache(test_url))
    # test_url = 'https://rumbler.ru' # рамблер  меня тоже отшил в процессе отладки, надо было таймаутов добавить
    print(check_cache(test_url))
    print(check_cache(test_url))
    print(get_data('hashes'))


    # не знаю как показать что все работает,  там база с одной табличкой...  по  идее (get_data('hashes')) возвращает
    # примерно такой лист: [(1, 'geekbrains.ru', ''), (4, 'https://geekbrains.ru', ''),
    # (5, 'https://google.ru', '6bbce80f013a55d6f486c7e47ce80d60a0c3545786b172682b8a2419b6c50bc1'),
    # (8, 'https://mail.ru', '1b9057c46bc6d2faef90b5f4e5d4be60e87ed52e1548aadc1f8fd97d0b42b3bd')]
    # добавил get_data_mok()
    # если поменять get_data на get_data_mok и закомментить write_data  в check_cache то все должно работать.

