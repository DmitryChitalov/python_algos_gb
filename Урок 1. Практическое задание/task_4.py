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

# Вывод: первый варинт эфективнее, т.к. быстрее

user_data = {
    'user1': {'pswd': '123456', 'activation': True},
    'user2': {'pswd': '123456', 'activation': False}
}


# Первый вариант. Сложность = O(1)
def authorization_1(users, user_name, user_pswd):
    if users.get(user_name):
        if users[user_name]['pswd'] != user_pswd:
            return f'Для пользователя {user_name} указан неверный пароль!'
        elif users[user_name]['pswd'] == user_pswd and not users[user_name]['activation']:
            return f'{user_name}, Вам необходимо активировать учетную запись!'
        elif users[user_name]['pswd'] == user_pswd and users[user_name]['activation']:
            return f'{user_name}, добро пожаловать в систему!'
    return f'Пользователя с именем "{user_name}" не найдено =('


# Второй варинат O(n)
def authorization_2(users, user_name, user_pswd):
    for key, val in users.items():
        if key == user_name:
            if val['pswd'] != user_pswd:
                return f'Для пользователя {user_name} указан неверный пароль!'
            elif val['pswd'] == user_pswd and not val['activation']:
                return f'{user_name}, Вам необходимо активировать учетную запись!'
            elif val['pswd'] == user_pswd and val['activation']:
                return f'{user_name}, добро пожаловать в систему!'
    return f'Пользователя с именем "{user_name}" не найдено =('


print(authorization_1(user_data, 'user1', '123'))
print(authorization_1(user_data, 'user1', '123456'))
print(authorization_1(user_data, 'user2', '123'))
print(authorization_1(user_data, 'user2', '123456'))
print(authorization_1(user_data, 'user3', '123'))

print(f'\n{"*" * 55}\n')

print(authorization_2(user_data, 'user1', '123'))
print(authorization_2(user_data, 'user1', '123456'))
print(authorization_2(user_data, 'user2', '123'))
print(authorization_2(user_data, 'user2', '123456'))
print(authorization_2(user_data, 'user3', '123'))
