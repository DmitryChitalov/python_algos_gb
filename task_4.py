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

users = {'user_1': {'password': '123456', 'active': True},
         'user_2': {'password': '123456', 'active': False},
         'user_3': {'password': '123456', 'active': True},
         'user_4': {'password': '123456', 'active': True}
         }


def authorization_1(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['active']:
                return "Доступ разрешен!"
            elif value['password'] == user_password and not value['active']:
                return "Запись не активирована!"
            elif value['password'] != user_password:
                return "Доступ запрещен!"

    return "Данного пользователя не существует"


print(authorization_1(users, 'user_3', '123456'))


def authorization_2(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['active']:
            return "Доступ разрешен!"
        elif users[user_name]['password'] == user_password and not users[user_name]['active']:
            return "Запись не активирована!"
        elif users[user_name]['password'] != user_password:
            return "Доступ запрещен!"
    else:
        return "Данного пользователя не существует"


print(authorization_2(users, 'user_3', '123456'))

#"Лучший вариант второй, т.к. первый вариант O(n), а второй O(1) и он быстрее"
