"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
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


def auth_1(login, password):  # Сложность этого метода O(n)
    global users
    if login in users:  # O(n)
        if users[login][0] != password:  # O(1)
            return 1, 'Не верный логин или пароль!'  # O(1)
        elif users[login][1]:  # O(1)
            return 0, f'{login}, добро пожаловать на сайт!'  # O(1)
        else:
            print('Ваша учетка не активирована!\nДоступ на сайт не активированной учетки запрещен!')  # O(1)
            ans = None  # O(1)
            while ans not in ('y', 'n'):  # O(n)
                ans = input('Активировать вашу учетку? (y/n): ').lower()  # O(1)
                if ans == 'y':  # O(1)
                    users[login] = (password, True)  # O(1)
                    return 2, f'{login}, ваша учетка активирована, можно авторизоваться!'  # O(1)
                elif ans == 'n':  # O(1)
                    return 3, f'{login}, ваша учетка не активирована!\nАвторизуйтесь и пройдите активацию.'  # O(1)
    else:
        return 1, 'Не верный логин или пароль!'  # O(1)


def auth_2(login, password):  # Сложность этого метода O(1)
    global users
    try:
        user = users[login]  # O(1)
    except KeyError:
        return 1, 'Не верный логин или пароль!'  # O(1)
    if user[0] != password:  # O(1)
        return 1, 'Не верный логин или пароль!'  # O(1)
    if user[1]:  # O(1)
        return 0, f'{login}, добро пожаловать на сайт!'  # O(1)
    else:
        print('Ваша учетка не активирована!\nДоступ на сайт не активированной учетки запрещен!')  # O(1)
        ans = None  # O(1)
        while ans not in ('y', 'n'):  # O(1)
            ans = input('Активировать вашу учетку? (y/n): ').lower()  # O(1)
            if ans == 'y':  # O(1)
                users[login] = (password, True)  # O(1)
                return 2, f'{login}, ваша учетка активирована, можно авторизоваться!'  # O(1)
            elif ans == 'n':  # O(1)
                return 3, f'{login}, ваша учетка не активирована!\nАвторизуйтесь и пройдите активацию.'  # O(1)


"""
Вывод: эффективнее второй способ, т.к. в нем мы ушли от поиска по словарю.
"""

f = auth_1  # Здесь можно выбрать один из алгоритмов авторизации (auth_1, auth_2)

users = {
    'vasia': ('qwerty', False),
    'petia': ('ytrewq', False),
    'kolia': ('wqreyt', False),
    'olia': ('tyerqw', False),
    'egor': ('123qwe', True),
    'makar': ('qwe123', True),
    'ostap': ('q1w2e3r4', True)
}
while True:
    a = input('Желаете войти на сайт? (y/n): ').lower()
    if a == 'n':
        break
    if a == 'y':
        l = input('Введите логин: ')
        p = input('Введите пароль (его будет видно): ')
        res, msg = f(l, p)
        print(msg)
        if not res:
            break
