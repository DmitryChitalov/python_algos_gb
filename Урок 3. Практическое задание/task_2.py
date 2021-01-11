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
import hashlib


login = hashlib.sha256(input('Введите логин:  ').encode('utf-8'))
password = hashlib.sha256(input('Пароль:  ').encode('utf-8'))
hash_obj = login.hexdigest()+password.hexdigest()
print(hash_obj)
file = open('password.txt', 'w')
file.write(hash_obj)
file.close()

def check_pass():
    password_rep = hashlib.sha256(input('Повторите пароль:  ').encode('utf-8'))
    hash_obj_rep = login.hexdigest() + password_rep.hexdigest()
    file = open('password.txt')
    pass_checking = file.read()
    print(pass_checking)
    file.close()
    if hash_obj_rep == pass_checking:
        print('Вы ввели верный пароль!')
    else:
        print('Пароль не верный!')
        check_pass()


check_pass()