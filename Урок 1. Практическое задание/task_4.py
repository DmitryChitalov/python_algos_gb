"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


### Вариант 1. Пароль и отметка об активации учетной записи размещены в значении словаря

def user_verification(active_db: dict, username: str, password: str) -> dict:
    key = username
    if key in active_db.keys() and active_db[key] == [password, True]:
        print(f'Hello {username}')
    elif key in active_db.keys() and active_db[key] == [password, False]:
        active = input('Пользовватель не активен, активировать (y/n): ')
        if active == 'y':
            print(f'Hello {username}')
            active_db[key] = [password, True]
    elif key in active_db.keys() and active_db[key][0] != password:
        print('Неправильный пароль')
    elif key not in active_db.keys():
        reg = input('Хотите зарегистрироваться? (y/n): ')
        if reg == 'y':
            active_db[key] = [password, False]
            print('Учетная запись создана, для активации еще раз войдите в программу')
        else:
            print('До свидания!')
    return active_db  # O(N)


### Вариант 2. Пароль и логин размещены в ключе словаря

def database(user_db: dict, username: str, password: str) -> dict:
    user = (username, password)
    if user in user_db.keys() and user_db[user] == True:
        print(f'Hello {username}')
    elif user in user_db.keys() and user_db[user] == False:
        active = input('Пользовватель не активен, активировать (y/n): ')
        if active == 'y':
            print(f'Hello {username}')
            user_db[user] = True
    else:
        reg = input('Хотите зарегистрироваться? (y/n): ')
        if reg == 'y':
            user_db[user] = False
            print('Учетная запись создана, для активации еще раз войдите в программу')
        else:
            print('До свидания!')
    return user_db  # O(N)


""" Второй вариант быстрее, а первый удобнее для пользователя """

active_db = {
    'Bill': ['236', False],
    'Nik': ['123', True],
}
user_db = {
    ('Bill', '236'): False,
    ('Nik', '123'): True,
}
username = input('Enter your name: ')
password = input('Enter password: ')
user_verification(active_db, username, password)
database(user_db, username, password)
print(user_db)
print(active_db)
