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

# Первое решение. Здесь сложность алгоритма реализации за счет цикла - O(N)
def authentification1(users, login, user_password):
    for key, value in users.items():
        if key == login:
            if value['password'] == user_password and value['verification']:
                return 'Welcome, your data is correct!'
            elif value['password'] == user_password and not value['verification']:
                return 'Sorry but your data is not correct! Please pass a verification!'
            elif value['password'] != user_password:
                return 'Password is not valid'
    return 'This login does not exist!'


# Второе решение. Здесь сложность алгоритма реализации - константная О(1). Функция get дает константную сложность, как и
# все остальное.
def authentification2(users, login, user_password):
    if users.get(login):
        if users[login]['password'] == user_password and users[login]['verification']:
            return 'Welcome, your data is correct!'
        elif users[login]['password'] == user_password and not users[login]['verification']:
            return 'Sorry but your data is not correct! Please pass a verification!'
        elif users[login]['password'] != user_password:
            return 'Password is not valid'
    else:
        return 'This login does not exist!'

# Второе решение лучше первого: реализация быстрее, т.к. проще сложность алгоритма - О(1) против О(N).


users_dict = {'user1': {'password': 'qwerty', 'verification': True},
            'user2': {'password': 'ytrewq', 'verification': True},
            'user3': {'password': 'abcde', 'verification': True},
            'user4': {'password': '12345', 'verification': False}
            }

print(authentification1(users_dict, 'user2', 'ytrewq'))

print(authentification2(users_dict, 'user4', '12345'))