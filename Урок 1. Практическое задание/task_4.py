"""
Задание 4.

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

users = {'user1': {'passwd': '123', 'status': True},
         'user2': {'passwd': '321', 'status': False}
         }

#O(1)
def auth(users, user_name, user_passwd):
    if users.get(user_name):
        if users[user_name]['passwd'] == user_passwd and users[user_name]['status']:
            print("hello")
        elif users[user_name]['passwd'] == user_passwd and not users[user_name]['status']:
            print("login is not active")
        elif users[user_name]['passwd'] != user_passwd:
            print("password is bad")
    else:
        return "user does not exist"

user_name = input("login: ")
user_passwd = str(input("password: "))

auth(users, user_name, user_passwd)
