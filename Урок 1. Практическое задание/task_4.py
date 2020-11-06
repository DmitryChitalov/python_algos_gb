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


"""
Решение 1:
Сложность: O(N^2)
"""

def autentificator(login, password):
    total_phrase = None
    activation = None
    users_base = {
        'Todd Howard': 'Bethesda rules',
        'Tim Sweeney': 'We are against apple',
        'Phil Spencer': 'x-box is a future'
    }
    users_activate = {
        'Todd Howard': 'activated',
        'Tim Sweeney': 'deactivated',
        'Phil Spencer': 'deactivated'
    }

    base_len = 0
    for k, v in users_base.items():
        base_len = base_len + 1
        if login == k and password == v:
            for k, v in users_activate.items():
                if login == k:
                    activation = v
            if activation == 'activated':
                total_phrase = "Добро пожаловать, ", login, "!"
            else:
                total_phrase = "Добро пожаловать, ", login, "! Перед входом в систему пройдите активацию."
    if base_len >= 3 and total_phrase == None:
        total_phrase = "Неправильный логин или пароль"

    return total_phrase

login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")

autentification = autentificator(login, password)
print(autentification)


"""
Решение 2:
Сложность: O(N)
"""
def autentification_program(login, password):
    end_phrase = None
    users_base = {
        'Todd Howard': ['Bethesda rules', 'activated'],
        'Tim Sweeney': ['We are against apple', 'deactivated'],
        'Phil Spencer': ['x-box is a future', 'deactivated']
    }
    base_len = 0
    for k, v in users_base.items():
        base_len = base_len + 1
        if login == k and password == v[0]:
            end_phrase = "Добро пожаловать, ", login, "!"
            if v[1] != 'activated':
                end_phrase = "Добро пожаловать, ", login, "! Перед входом в систему пройдите активацию."
    if base_len >= 3 and end_phrase == None:
        end_phrase = "Неправильный логин или пароль"
    return end_phrase


login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")

autentification = autentification_program(login, password)
print(autentification)

"""Второе решение эффективнее по ряду причин:
    1) В качестве хранилища использован один словарь, вместо двух. К сожалению, не могу оценить
    с позиции безопасности, но что-то мне подсказывает, что первый вариант безопаснее.
    2) Решение проще, нет вложенных циклов
    3) По объему меньше, проще читать
"""
