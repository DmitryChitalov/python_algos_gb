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


""" Решение 1. Сложность O(1)"""

user_data = {'ivanpetrov': {'name': 'Ivan Petrov', 'login': 'ivanpetrov', 'password': 'qwerty', 'activated': True},
             'petrivanov': {'name': 'Petr Ivanov', 'login': 'petrivanov', 'password': '12345', 'activated': False}}


def auth(login, password):
    if login in user_data.keys():
        if password == user_data.get(login).get('password'):
            if user_data.get(login).get('activated')==True:
                print(f'Добро пожаловать, {user_data.get(login).get("name")}')
            else:
                print('Вам необходимо активировать учётную запись.')
        else:
            print('Неверный пароль!')
    else:
        print('Пользователь с таким имененм не найден.')


auth('ivanpetrov', 'qwerty')




"""Решение 2. Сложность O(1))"""


class UserData:

    def __init__(self, name, login, password, activated: bool):
        self.name = name
        self.login = login
        self.password = password
        self.activated = activated

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def check_activation(self, login):
        if self.activated == True:
            return True
        else:
            return False


def find_user(login):
    if login in userbase.keys():
        return userbase.get(login)
    else:
        return None


def authorization(user_login, user_password):
    user = find_user(user_login)
    if user is None:
        print('Пользователь с таким логином не найден.')
    else:
        if user.check_password(user_password) is False:
            print('Пароль неверный.')
        else:
            if user.check_activation(user_login) is False:
                print('Пожалуйста, активируейте свою учетную запись.')
            else:
                print(f'Добро пожаловать, {find_user(user_login).name}')


sidorsidorov = UserData('Sidor Sidorov', 'sidorsidorov', 'qweasd', True)
ivanivanov = UserData('Ivan Ivanov', 'ivanivanov', '123456', False)

userbase = {}
userbase['sidorsidorov'] = sidorsidorov
userbase['ivanivanov'] = ivanivanov

authorization('sidorsidorov', 'qweasd')
