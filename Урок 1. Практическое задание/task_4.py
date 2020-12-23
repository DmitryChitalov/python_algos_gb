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


# var.1 сложность получилась O(1) поскольку применяются только конструкции if else в решении
# Вложенность if в if не услодняет само решение. Работа функции происходит только по поиску в словаре ключа O(1)


def autorization_if(data_users, login, password):
    if data_users.get(login):
        if data_users[login]['pass'] == password and data_users[login]['active']:
            return 'Welcome! Your account is active'
        elif data_users[login]['pass'] != password:
            return 'Incorrect password'
        elif data_users[login]['pass'] == password and not data_users[login]['active']:
            return 'Your account is not active!'
    else:
        return 'The user does not exist'


# var.2 усложненный вариант var.1 - за счет цикла - общая сложность будет O(n)


def autorization_for_if(data_users, user_login, user_password):
    for login, value in data_users.items():
        if login == user_login:
            if value['pass'] == user_password and value['active']:
                return 'Welcome! Your account is active'
            elif value['pass'] == user_password and not value['active']:
                return 'Your account is not active!'
            elif value['pass'] != user_password:
                return 'Incorrect password'

    return 'The user does not exist'


users = {'login1': {'pass': '12345', 'active': True},
         'login2': {'pass': '12345', 'active': True},
         'login3': {'pass': '12345', 'active': True},
         'login4': {'pass': '12345', 'active': False},
         'login5': {'pass': '12345', 'active': False},
         'login6': {'pass': '12345', 'active': False}
         }

print(autorization_if(users, 'login1', '12345'))
print(autorization_if(users, 'login4', '12345'))
print(autorization_if(users, 'login7', '12345'))

print(autorization_for_if(users, 'login1', '12345'))
print(autorization_for_if(users, 'login4', '12345'))
print(autorization_for_if(users, 'login7', '12345'))

# вывод - var.1 с функцией autorization_if очевидно более оптимальное решение - O(1) лучше, чем с O(n)