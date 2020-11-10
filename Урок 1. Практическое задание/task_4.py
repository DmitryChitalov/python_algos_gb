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


# Cложность  O(1) - константа

def auth_user(users_db, usr_name, usr_pass):
    if users_db.get(usr_name):
        if users_db[usr_name]['pass'] == usr_pass and users_db[usr_name]['activation']:
            return print(f'Welcome {usr_name}')
        elif users_db[usr_name]['pass'] == usr_pass and not users_db[usr_name]['activation']:
            return print(f'{usr_name} your account is not active!')
        elif users_db[usr_name]['pass'] != usr_pass:
            return print(f'{usr_name} your password is wrong')
    else:
        return print(f"Can't find user")

# Cложность  O(n) - линейная

def auth_user2(users_db, usr_name, usr_pass):
    for key, value in users_db.items():
        if key == usr_name:
            if value['pass'] == usr_pass and value['activation']:
                return print(f'Welcome {usr_name}')
            elif value['pass'] == usr_pass and not value['activation']:
                return print(f'{usr_name} your account is not active!')
            elif value['pass'] != usr_pass:
                return print(f'{usr_name} your password is wrong')

    return print(f"Can't find user")


users_db = {'michael': {'pass': '1', 'activation': True},
            'bob': {'pass': '2', 'activation': True},
            'tom': {'pass': '3', 'activation': False},
            }
auth_user(users_db, 'tom', '3')
auth_user2(users_db, 'tom', '3')