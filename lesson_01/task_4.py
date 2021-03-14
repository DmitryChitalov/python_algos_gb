"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
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

# Пусть хранение данных будет реализовано в виде словаря:

test_dict = {
    'Masha': {'password': '123', 'activated': True},
    'Dino747': {'password': '456', 'activated': True},
    'Zanuda_over_9000': {'password': 'bHyuL3oih0J8N190fd', 'activated': True},
    'User_user': {'password': '111111', 'activated': False},
    'Simka': {'password': 'tralala1', 'activated': True},
    'Kotik': {'password': '999666', 'activated': False}
}


def user_authorization_1(users_dict: dict, login: str, password: str):
    """
    Функция осуществляет проверку, может ли пользователь быть допущен к ресурсу.
    :param users_dict: словарь с данными пользователей
    :param login: логин пользователя
    :param password: введённый пользователем пароль
    :return: None
    Сложность: O(N) - линейная
    """
    if login in users_dict:  # O(N)
        user_pass = users_dict[login].get('password')  # O(1)
        user_status = users_dict[login].get('activated')  # O(1)

        if user_pass == password and user_status:    # O(1)
            print('Доступ разрешён!')  # O(1)

        elif not user_pass == password:  # O(1)
            print('Доступ запрещён! Введён неверный пароль!')  # O(1)

        else:  # O(1)
            print('Доступ запрещён! Учётная запись не активирована.')  # O(1)
            user_answer = input('Желаете активировать учётную запись? (д/н)')  # O(1)

            if user_answer.lower() == 'д':  # O(1)
                users_dict[login]['activated'] = True  # O(1)
                print('Учётная запись активирована. Доступ разрешён.')  # O(1)

            else:  # O(1)
                print('Доступ запрещён.')  # O(1)

    else:  # O(1)
        print('Логин пользователя указан неверно.')  # O(1)


# Можно реализовать хранение данных в виде списка:

test_list = [
    'Masha', '123', True,
    'Dino747', '456', True,
    'Zanuda_over_9000', 'bHyuL3oih0J8N190fd', True,
    'User_user', '111111', False,
    'Simka', 'tralala1', True,
    'Kotik', '999666', False
]


def user_authorization_2(users_list: list, login: str, password: str):
    """
    Функция осуществляет проверку, может ли пользователь быть допущен к ресурсу.
    :param users_list: список с данными пользователей
    :param login: логин пользователя
    :param password: введённый пользователем пароль
    :return: None
    Сложность: O(N) - линейная
    """
    logins = [users_list[idx] for idx in range(0, len(users_list), 3)]  # O(N)
    passwords = [users_list[idx] for idx in range(1, len(users_list), 3)]  # O(N)
    statuses = [users_list[idx] for idx in range(2, len(users_list), 3)]  # O(N)

    try:  # O(1)

        idx = logins.index(login)  # O(1)
        user_pass = passwords[idx]  # O(1)
        user_status = statuses[idx]  # O(1)

        if password != user_pass and user_status:  # O(1)
            print('Доступ запрещён! Введён неверный пароль!')  # O(1)

        if password == user_pass and not user_status:  # O(1)
            print('Доступ запрещён! Учётная запись не активирована.')  # O(1)
            user_answer = input('Желаете активировать учётную запись? (д/н)')  # O(1)

            if user_answer.lower() == 'д':  # O(1)
                users_list[idx*3 + 2] = True  # O(1)
                print('Учётная запись активирована. Доступ разрешён.')  # O(1)

            else:  # O(1)
                print('Доступ запрещён.')  # O(1)

        if password != user_pass and not user_status:  # O(1)
            print('Доступ запрещён! Введён неверный пароль!')  # O(1)

        if password == user_pass and user_status:  # O(1)
            print('Доступ разрешён!')  # O(1)

    except ValueError:  # O(1)
        print('Неверный логин!')  # O(1)


user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')

# Вывод: обе функции имеют линейную сложность, но первая функция будет предпочтительнее.
# Вторая функция работает со списком по индексам, чего следует по возможности избегать, кроме того,
# в ней создаётся множество промежуточных объектов и имеется избыточность в построении условий.
