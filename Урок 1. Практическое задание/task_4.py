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


users = {'Gold': ['345654fr', 'active'], 'Valencia': [6453632, 'active'],
         'Rasmerus': ['gfhdn354' 'not active'], 'Jolerno': ['gfhe876', 'active']}

"""
Функция имеет сложность n^3, тратит много времени на реализацию.
"""


# Сложность: O(n ** 3)


def security_one(user):
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    for i in user.items():
        if login in i and password == str(i[1][0]):
            if i[1][1] == 'active':
                print("Вход разрешён.")
            else:
                print("Активируйте учетную запись.")


security_one(users)

########################################################################################################################

users = [['Gold', '345654fr', 'active'], ['Valencia', '6453632', 'active'],
         ['Rasmerus', 'gfhdn354', 'not active'], ['Jolerno', 'gfhe876', 'active']]

"""
Имеет ту же степень сложности, что и предыдущая функция.
Изменён способ хранения данных. Код более прост в понимании,
но особо не отличается. 
"""


# Сложность: O(n ** 3)


def security_two(user):
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    for i in user:
        if login in i and password in i:
            if 'active' in i:
                print("Вход разрешён.")
            else:
                print("Активируйте учётную запись.")


security_two(users)