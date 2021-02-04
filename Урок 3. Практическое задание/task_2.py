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


from hashlib import sha256


def get_hashed_pwd(user, password):
    return sha256((user + password).encode('utf-8')).hexdigest()


def save_pwd(password):
    with open("pw_db.txt", 'w+') as f:
        f.write(password)


def load_pwd():
    with open("pw_db.txt") as f:
        return f.read()


print('Введите пользователя')
usr = input()
print('Введите пароль')
pwd = input()
hashed = get_hashed_pwd(usr, pwd)
save_pwd(hashed)
print(f'Зашифрованный пароль {hashed}')
print('Введите пароль еще раз для проверки')
pwd2 = input()
hashed2 = get_hashed_pwd(usr, pwd2)

if hashed == hashed2:
    print('Пароли совпадают')
else:
    print('Пароли не совпадают')
