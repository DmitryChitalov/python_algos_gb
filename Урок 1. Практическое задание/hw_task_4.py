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

system_users = {
    'names': ['vasiliy', 'fedor', 'grigoriy'],
    'vasiliy': {'login': 'vas', 'password': 'vas1', 'activate': True},
    'fedor': {'login': 'fed', 'password': 'fed1', 'activate': False},
    'grigoriy': {'login': 'gri', 'password': 'gri1', 'activate': True}
}


# vasiliy = {
#     'login': 'vas',
#     'password': 'vas1',
#     'activate': True,
#     }

# fedor = {
#     'login': 'fed',
#     'password': 'fed1',
#     'activate': False,
#     }

# grigoriy = {
#     'login': 'gri',
#     'password': 'gri1',
#     'activate': True,
#     }

# users = ['vasiliy', 'fedor', 'grigoriy']
def logon1(*args):  # O(2n**2)
    step_1 = input('Введите имя пользователя: ')  # O(1)
    for i in system_users.get('names'):  # O(n)
        while step_1 not in system_users.get('names'):  # O(n)
            print('Такого пользователя не существует')
            step_1 = input('Введите имя пользователя: ')  # O(1)

    if (system_users.get(step_1)).get('activate'):  # O(n)
        step_2 = input('Введите логин: ')  # O(1)
        while step_2 != ((system_users.get(step_1)).get('login')):  # O(n)
            print('Логин неверный')
            step_2 = input('Введите логин: ')  # O(1)
        step_3 = input('Введите пароль: ')  # O(1)
        while step_3 != ((system_users.get(step_1)).get('password')):  # O(n)
            print('Пароль неверный')
            step_3 = input('Введите пароль: ')  # O(1)
    else:
        print('Активируйте аккаунт по ссылке в письме')


logon1()


####################################################################

def logon2(s_users, u_name, u_password):  # O(n)
    for key, value in s_users.items():  # O(n)
        if key == u_name:
            if value['password'] == u_password and value['activate']:
                return 'Добро пожаловать!'
            elif value['password'] == u_password and not value['activate']:
                return 'Активируйте аккаунт по ссылке в письме'
            elif value['password'] != u_password:
                return 'Пароль неверный'

    return 'Пользователь не найден'


print(logon2(system_users, 'grigoriy', 'gri1'))

#  Я бы все-равно выбрал первое решение, оно взаимодействует с пользователем. Но, второе видимо лучше.
