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

user_log = {'login': ['Nik', 'John'], 'password': ['123', '444'], 'is_active': [False, True]}

"""T(n) = 6n + 7
Общая сложность O(n)"""


def validation():
    log_in = input('Введите логин: ').capitalize()  # O(1)
    if log_in in user_log['login']:  # O(n)
        password = input(f'Пользователь {log_in} введите пароль: ')  # O(1)
        login_id = user_log['login'].index(log_in)  # получаем индекс элемента (логина для сравнения с паролем) # O(1)
        if password == user_log['password'][login_id]:  # O(n)
            if user_log['is_active'][login_id]:  # O(n)
                print('Добро пожаловать!')  # O(1)
            else:  # O(n)
                print('Ваша учетная запись не активирована\nПожалуйста, пройдите валидацию')  # O(1)
        else:  # O(n)
            print('*** Пароль не подходит ***')  # O(1)
    else:  # O(n)
        print('*** Такой пользователь не зарегистрирован ***')  # O(1)


validation()
print()

"""T(n) = 5n + 12
Общая сложность O(n)"""
"""В первом решении если логин верный, то получаем индекс логина в словаре, и запрашиваем пароль 
Во втором случае получаем индексы логина и пароля, и уже сравниваем эти цифры между собой
Считаю первое решение более эффективным, т.к. если логина нет в словаре, то и искать дальше нет смысла и требуется 
 на 5 констант меньше"""

def validation_2():
    log_in = input('Введите логин и пароль через пробел: ').split()  # O(1)
    if len(log_in) < 2:  # O(n)
        print('Вы ввели не все данные')  # O(1)
    else:  # O(n)
        user_name = log_in[0].capitalize()  # O(1)
        password = log_in[1]  # O(1)
        try:  # O(1)
            login_id = user_log['login'].index(user_name)  # O(1)
            password_id = user_log['password'].index(password)  # O(1)
            if (login_id == password_id) and user_log['is_active'].index(login_id):  # O(n)
                print('Добро пожаловать!')  # O(1)
            elif (login_id == password_id) and not user_log['is_active'].index(login_id):  # O(n)
                print('Ваша учетная запись не активирована')  # O(1)
            else:  # O(n)
                print('Логин или пароль указаны не верно')  # O(1)
        except ValueError:  # O(1)
            print('Логин или пароль указаны не верно')  # O(1)


validation_2()
