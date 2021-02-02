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


data = {'john': ['qwerty', True], 'lisa': ['12wer', False], 'andrei': ['15letauf', True],
        'spiderman': ['thereal1', False]}


def resolution_1(database, user, password):
    for nick, info in database.items():
        if user == nick:
            if (password == info[0]) and (info[1] is True):
                return 'You have been succesfully logged in'
            elif password == info[0] and info[1] is False:
                return 'Refused in logging in. Please activate your account first'
            elif password != info[0] and info[1] is False:
                return 'Your password is incorrect. Additionally, activate your account before next log in'
            elif password != info[0] and info[1] is True:
                return 'Your password is incorrect'
        else:
            return f"User with nickname \"{user}\" does not exist in the system"


def resolution_2(database, user, password):
    try:
        user_data = database[user]
        if user_data[0] == password and user_data[1] is True:
            return 'You have been succesfully logged in'
        elif user_data[0] == password and user_data[1] is False:
            return 'Refused in logging in. Please activate your account first'
        elif user_data[0] != password and user_data[1] is False:
            return 'Your password is incorrect. Additionally, activate your account before next log in'
        elif user_data[0] != password and user_data[1] is True:
            return 'Your password is incorrect'
    except KeyError:
        return 'User does not exist'


print(resolution_1(data, 'john', 'qwety'))
print(resolution_2(data, 'john', 'qwety'))


# Ответ: resolution_1 сложность O(n)
#        resolution_2 сложность 0(1)
# Более оптимальным вариантом будет второе решение так как на его исполнение требуется меньше ресурсов и не требуется
# цикл перебора for.
