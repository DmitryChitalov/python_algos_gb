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
# from hashlib import sha256
from uuid import uuid4
import hashlib

pass_db = open('hash_file_for_task02.txt', 'w')
pasword = input("Введите пароль: ").encode('utf-8')
sal = uuid4().hex


# print(sal)


def user_password(pas, salt, db):
    result_passw0rd = hashlib.sha256(salt.encode() + pas).hexdigest()
    #print(f'В базе данных хранится строка: {result_passw0rd}')
    db.writelines(result_passw0rd + '\n')
   # return result_passw0rd


user_password(pasword, sal, pass_db)

pass_check = input("Введите пароль еще раз для проверки: ").encode('utf-8')
user_password(pass_check, sal, pass_db)
pass_db.close()
#lines= print(pass_db.readlines())

check = open('hash_file_for_task02.txt', 'r')
lines = check.readlines()
print(f'В базе данных хранится строка: {lines[0]}')
#print(lines)


if lines[0] == lines[1]:
    print("Вы ввели правильный пароль")
else:
    print("Вы ввели не правильный пароль")

check.close()


"""_________________________________________________________________________"""