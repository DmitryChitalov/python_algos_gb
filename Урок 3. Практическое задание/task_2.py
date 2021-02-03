"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from hashlib import pbkdf2_hmac
from binascii import hexlify
from platform import node


def calc_super_hash(i_pass):
    i_pass = i_pass.encode('utf-8')
    l_obj = pbkdf2_hmac(hash_name='sha256',
                        password=i_pass,
                        salt=node().encode('utf-8'),
                        iterations=100000)
    l_res = hexlify(l_obj)
    return l_res


def write_super_hash(i_data):
    with open('super_hash.txt', 'wb') as f:
        f.write(i_data)


def read_super_hash():
    with open('super_hash.txt', 'rb') as f:
        return f.read()


g_pass_01 = input('Введите пароль: ')
write_super_hash(calc_super_hash(g_pass_01))
g_from_file_01 = read_super_hash()

print('В базе данных хранится строка: ', g_from_file_01.decode())
g_pass_02 = input('Введите пароль еще раз для проверки: ')
g_hash_02 = calc_super_hash(g_pass_02)

if g_from_file_01 == g_hash_02:
    print('Вы ввели правильный пароль.')
else:
    print('Вы ввели неправильный пароль!')
