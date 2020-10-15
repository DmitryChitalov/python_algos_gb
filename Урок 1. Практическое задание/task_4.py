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


def authorization(users: dict, user_name: str, user_password: str) -> str:
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return 'Welcome! Enjoy our resource!'
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:
            return 'Please complete activation to continue.'
        elif users[user_name]['password'] != user_password:
            return 'Your password is incorrect.'
    else:
        'This user dose not exist'


my_users = {
    'user1': {'password': '12345678', 'activation': True},
    'user2': {'password': '12345678', 'activation': True},
    'user3': {'password': '12345678', 'activation': False},
    'user4': {'password': '12345678', 'activation': True},
    'user5': {'password': '12345678', 'activation': False},

}

