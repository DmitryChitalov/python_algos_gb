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

import random
# выбираем следующую структуру:{логин: [пароль, отметка об активации]}
# для разовой генерации датасета сделал отдельную функцию:


def create_dict_data_base(user_numbers):
    dict_data_base = {}
    logins_list = []
    pass_list = []
    activation_list = []
    values_dict = []
    # генерируем случайные логины
    for k in range(user_numbers):
        login = ''
        for i in range(0, 5):
            login += chr(random.randint(65, 90)).lower()
        logins_list.append(login)
    # генерируем случайные пароли
    for idx in range(user_numbers):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        passwd = ''
        for j in range(0, 8):
            passwd += random.choice(chars)
        pass_list.append(passwd)
    # генерируем случайным образом отметку об авторизации: 1 - есть авторизация, 1 - нет авторизации
    activation_list = [random.randint(0, 1) for i in range(user_numbers)]
    # собираем пароли и данные об авторизации по парам и записываем в список по 2
    for k in range(len(activation_list)):
        values_dict.append([pass_list[k], activation_list[k]])
    # формируем финальный словарь с нашими данными
    dict_data_base = dict(zip(logins_list, values_dict))
    return dict_data_base

# следующей строкой вызываем функцию для генерации базы данных, далее из консоли можно скопировать данные в словарь
# dict_1 = create_dict_data_base(5)


# для тестов оставил один вариант словаря:
dict_1 = {
    'gwfrd': ['Blh6F<a#', 0],
    'vwkgu': ['ro9EW<ib', 0],
    'xqnvl': ['6*2v1I?5', 0],
    'gfwst': ['+Da/!PeG', 1],
    'quhuq': ['EqF!g!ZP', 0]
}

# Выводим словарь в удобном виде
print('Our data base is:')
for key, value in dict_1.items():
    print(f'\t{key}: {value}')
print('-----------------')


# 1-й вариант: разобьем функцию проверки на несколько блоков и каждый оформим в виде отдельной функции.
# при смене логики входа пользователей так легче будет переносить блоки, читается легче, легче поддерживать код.
# Сложность получилась O(n)


def check_user_login (user_login, user_dict):
    """
    Функция проверяет существования пользователя.

    Принимает парметры:
    user_login: str
    user_dict: dict
    В случае существования пользователя/корректности логина возвращает True

    Сложность: O(n)
    """
    for key in user_dict.keys():
        if user_login == key:
            return True


def check_user_activation (user_login, user_dict):
    """
    Функция проверяет активацию учетной записи пользователя.
    Принимает парметры:
    user_login: str
    user_dict: dict
    В случае если учетная запись пользователя с указанным логином активирована, то функция возвращает True
    Сложность: O(1)
    """
    if user_dict[user_login][1] == 1:
        return True


def check_user_password (user_login, user_pass, user_dict):
    """
    Функция проверяет корректность пароля пользователя.

    Принимает парметры:
    user_login: str
    user_pass: str
    user_dict: dict
    В случае если пароль верный, функция возвращает True

    Сложность: O(1)
    """
    if user_dict[user_login][0] == user_pass:
        return True


def user_activation(user_login, user_dict):
    """
    Функция-заглушка для обозначения активации учетной записи пользователя.

    Принимает парметры:
    user_login: str
    user_dict: dict

    Пока ничего не делает, поэтому сложность нельзя определить.
    """
    user_act_answer = input('Хотите пройти активацию сейчас? Введите "да": ')
    if user_act_answer.lower() == 'да':
        pass
        print(f'Ваша учетная запись активирована, теперь вы сможете войти')
    else:
        print('Значит в следующий раз')


def check_user_enter_1 (user_login, user_pass, user_dict):
    """
    Итоговая функция, проверяющая авторизацию.

    Принимает парметры:
    user_login: str
    user_pass: str
    user_dict: dict
    В данном виде функция возвращает True если доступ разрешен.

    Сложность: O(n)
    """
    if check_user_login(user_login, user_dict):
        if check_user_activation(user_login, user_dict):
            if check_user_password(user_login, user_pass, user_dict):
                print('Доступ разрешен')
                return True
            else:
                print('Неверный пароль')
        else:
            print('Ваша учетная запись не активирована. Ждя входа необходимо её активировать.')
            user_activation(user_login, user_dict)
    else:
        print('Такого пользователя не существует')


# 2-й вариант решения задачи
# тут производим все проверки в одном блоке, проходимся циклом по словарю: сразу видно, что такой код читается сложнее
# и при смене логики придется вносить серьезные изменения. Также пришлось break вставить, а я очень не люблю его))
# Кстати говоря, сложность тут тоже O(n) получается вроде. Но код мне меньше нравится.
def check_user_enter_2(user_login, user_pass, user_dict):
    """
    2-й вариант функции, проверяющей авторизацию.

    Принимает парметры:
    user_login: str
    user_pass: str
    user_dict: dict
    Функция возвращает True если доступ разрешен.

    Сложность: O(n)
    """
    res = False
    for key, value in user_dict.items():
        if key == user_login and value[0] == user_pass and value[1] == 1:
            res = True
            break
        elif key == user_login and value[0] == user_pass and value[1] == 0:
            print('Для входа требуется произвести активацию вашей учётной записи.')
            user_activation_answer = input('введите "да" для прохождения активации: ')
            if user_activation_answer.lower() == 'да':
                pass
                print('Активация пройдена успешно!')
                res = True
    if res == True:
        print('Доступ разрешен')
        return True
    else:
        print('Неверное имя пользователя или пароль:(')

#check_user_enter_1('quhuq', 'EqF!g!ZP', dict_1)
check_user_enter_2('gwfrd', 'Blh6F<a#', dict_1)




