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

def check_pass():
    """ Запрашивает пароль, делает хеш пароля, сверяет хеши паролей"""
    psw1 = input("Введите пароль: \n")

    salt_str = hashlib.sha256(b"It's no moon").hexdigest()
    hash_ps = hashlib.sha256((psw1).encode('utf-8')).hexdigest()

    bd_str = hash_ps + ':' + salt_str # храним через разделитель хеш пароля и соль

    print("В базе данных хранится строка: \n", bd_str)

    psw2 = input("Введите пароль еще раз для проверки: \n")

    hash_ps2 = hashlib.sha256((psw2).encode('utf-8')).hexdigest()

    ver_str =  hash_ps2 + ':' + salt_str

    if ver_str == bd_str:
        return print("Вы ввели правильный пароль! ")
    else:
        return print("Указан неверный пароль")
    return

def check_pass2():
    """ Запрашивает пароль, делает хеш пароля, сверяет хеши паролей"""
    psw1 = input("Введите пароль: \n")

    salt_str = 'This is the Way'
    hash_ps = hashlib.sha256((psw1+salt_str).encode('utf-8')).hexdigest()

    bd_str = hash_ps # присоединяем соль к паролю (пароль и соль не разделить)

    print("В базе данных хранится строка: \n", bd_str)

    psw2 = input("Введите пароль еще раз для проверки: \n")

    hash_ps2 = hashlib.sha256((psw2+salt_str).encode('utf-8')).hexdigest()

    ver_str =  hash_ps2

    if ver_str == bd_str:
        return print("Вы ввели правильный пароль! ")
    else:
        return print("Указан неверный пароль")
    return

# клиентская часть

if __name__ == "__main__":
    check_pass()
    check_pass2()