"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание: Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты
2 и 3 можно выполнить через строки документации в самом коде. Если у вас
возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)". Алгоритмизатор должен развивать мышление,
а это прежде всего практика. А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано
в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


def authentication_func(login: str, password: str, base: list) -> bool:
    """
    Вариант 1 - Сложность O(N)

    Функция проверяет наличие пользователя в базе, правильность ввода пароля,
    статус активации аккаунта, а также предлагает активировать аккаунт,
    если активация не выполнена

    Функция принимает на вход 3 параметра:
    - логин пользователя
    - пароль пользователя
    - список словарей, содержащих информацию о пользователе

    Функция возвращает значение True в случае успешной авторизации и
    False, если авторизация не удалась
    """
    for user_dict in base:  # O(N)
        if user_dict['login'] == login:  # O(1)
            if user_dict['password'] != password:  # O(1)
                print('Неверный пароль')  # O(1)
                return False  # O(1)
            is_active = user_dict['is_active']  # O(1)
            if not is_active:  # O(1)
                print('Необходимо активировать аккаунт')  # O(1)
                activation = input('Введите "Y" чтобы активировать: ')  # O(1)
                if activation.upper() != 'Y':  # O(1)
                    print('Аккаунт не активирован')  # O(1)
                    return False  # O(1)
                user_dict['is_active'] = True  # O(1)
                print('Аккаунт активирован')  # O(1)
            print('Аутентификация пройдена')
            return True  # O(1)

    print('Неверное имя пользователя')
    return False  # O(1)


def authentication_func_2(login: str, password: str, base: dict) -> bool:
    """
    Вариант 2 - Сложность O(1)

    Функция проверяет наличие пользователя в базе, правильность ввода пароля,
    статус активации аккаунта, а также предлагает активировать аккаунт,
    если активация не выполнена

    Функция принимает на вход 3 параметра:
    - логин пользователя
    - пароль пользователя
    - двухуровневый словарь, содержащий информацию о пользователе

    Функция возвращает значение True в случае успешной авторизации и
    False, если авторизация не удалась
    """
    try:
        user_info = base[login]  # O(1)
    except KeyError:
        print('Неверное имя пользователя')  # O(1)
        return False  # O(1)
    else:
        if user_info['password'] != password:  # O(1)
            print('Неверный пароль')  # O(1)
            return False  # O(1)
        is_active = user_info['is_active']  # O(1)
        if not is_active:  # O(1)
            print('Необходимо активировать аккаунт')  # O(1)
            activation = input('Введите "Y" чтобы активировать: ')  # O(1)
            if activation.upper() != 'Y':  # O(1)
                print('Аккаунт не активирован')  # O(1)
                return False  # O(1)
            user_info['is_active'] = True  # O(1)
            print('Аккаунт активирован')  # O(1)
        print('Аутентификация пройдена')  # O(1)
        return True  # O(1)


# На мой взгляд более быстрым выглядит второй вариант функции, так как его
# алгоритмическая скорость (если я все верно посчитала) = O(1), тогда как в 1
# варианте она = O(N). Однако я также видела мнение, что словари работают в
# каких-то случаях медленнее, чем списки, а также я не уверена, что обработка
# исключений не влияет на скорость выполнения кода. Также можно было
# попробовать написать ещё более медленный вариант функции, где несколько раз
# перебирались бы одни и те же словари или списки, но у меня не хватает на
# это времени и фантазии.

users_list = [
    {'login': 'anna', 'password': 'key', 'is_active': True},
    {'login': 'second', 'password': 'qwertY', 'is_active': False},
    {'login': 'japan', 'password': 'tokyo', 'is_active': True},
    {'login': 'xiaomi', 'password': 'redmi note IV', 'is_active': False}
]

# login_input = input('Имя пользователя: ').lower()
# password_input = input('Пароль: ')


authentication_func('anna', 'wrong', users_list)
authentication_func('japan', 'tokyo', users_list)
authentication_func('second', 'qwertY', users_list)
# authentication_func(login_input, password_input, users_list)

print('----------------------')

users_dict = {
    'anna': {'password': 'key', 'is_active': True},
    'second': {'password': 'qwertY', 'is_active': False},
    'japan': {'password': 'tokyo', 'is_active': True},
    'xiaomi': {'password': 'redmi note IV', 'is_active': False}
}

# login_input = input('Имя пользователя: ').lower()
# password_input = input('Пароль: ')

authentication_func_2('anna', 'wrong', users_dict)
authentication_func_2('japan', 'tokyo', users_dict)
authentication_func_2('second', 'qwertY', users_dict)
# authentication_func(login_input, password_input, users_dict)
