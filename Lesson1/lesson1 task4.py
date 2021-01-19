"""
Задание 4.
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

"""
#Решение взято из лекций

#Способ первый, общая сложность O(1)

def authorisation_easy(users, user_name, user_password):
    if users.get(user_name):
        if users[user_name]['password'] == user_password and users[user_name]['activation']:
            return "Заходите!"
        elif users[user_name]['password'] ==user_password and not users[user_name]['activation']:
            return "Пожалуйста, активируйте учетную запись"
        elif users[user_name]['password'] != user_password:
            return "Пароль неверный"
    else:
        return "Данного пользователя не существует."

data_users = {'user1': {'password': '122345', 'activation': True},
            'user2': {'password': '111111', 'activation': True},
            'user3': {'password': '77777', 'activation': True},
            'user4': {'password': '1141', 'activation': False}
            }

#Способ второй, общая сложность O(n)

def authorisation_hard(users, user_name, user_password):
    for key, value in users.items(): #n !!!!
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return "Заходите!"
            elif value['password'] == user_password and not value['activation']:
                return "Надо пройти активацию"
            elif value['password'] != user_password:
                return "Пароль неверный"
    return "Данного пользователя не существует"

print(authorisation_easy(data_users, 'user3', '123'))
print(authorisation_hard(data_users, 'user3', '77777'))

# Первый способ с фуенкцией get лучше (константная сложность)