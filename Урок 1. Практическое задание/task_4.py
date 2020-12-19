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

users = {
    'user_1': {'login': 'one', 'password': 'one_pass', 'activation': True},
    'user_2': {'login': 'two', 'password': 'two_pass', 'activation': False}
}


def verify_authentication_1(dict_obj, log, passw):
    list_items = list(dict_obj.items())
    for item in list_items:
        tmp_dict = item[1]
        if tmp_dict.get('login') == log:
            if tmp_dict.get('password') == passw and tmp_dict.get('activation') is True:
                return 'Добро пожаловать'
            elif tmp_dict.get('password') == passw and tmp_dict.get('activation') is False:
                return 'Учётная запись не активирована'
            elif tmp_dict.get('password') != passw:
                return 'неправильный пароль'
    return 'Такого пользователя не существует'


def verify_authentication_2(dict_obj, log, passw):
    list_items = list(dict_obj.items())
    for item in list_items:
        values_list = list(item[1].values())
        if log in values_list:
            if passw in values_list and True in values_list:
                return 'Добро пожаловать'
            elif passw in values_list and False in values_list:
                return 'Активируйте учётную запись'
            else:
                'Неправильный пароль'
    return 'Такого пользователя не существует'

"""
Функция verify_authentication_1 имеет сложность O(n) за счёт использования только одного цикла.
Функция verify_authentication_2 имеет сложность O(n**2) за счёт вложенного цикла в условии.
Из этих двух реализаций verify_authentication_1 является лучшей.
"""

if __name__ == '__main__':
    print(verify_authentication_1(users, 'one', 'one_pass'))
    print(verify_authentication_1(users, 'two', 'two_pass'))
    print(verify_authentication_1(users, 'three', 'three_pass'))
    print(verify_authentication_2(users, 'one', 'one_pass'))
    print(verify_authentication_2(users, 'two', 'two_pass'))
    print(verify_authentication_2(users, 'three', 'three_pass'))
