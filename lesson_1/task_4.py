"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.


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


# Сложность O(1)
def check_user(login_req):
    # поиск логина сложность O(1)
    curr_user = user_dict.get(login_req)
    if curr_user is None:
        print(f'Login {login_req} не найден. Доступ запрещен')
        return curr_user
    else:
        return curr_user


# Сложность O(1)
def check_user_password(lr, pr, up):
    while up != pr:
        print(f'Пароль для {lr} указан неверно')
        pr = str(input("Введите password или Q для выхода : "))
        if pr == 'Q':
            return False
    return True


# Сложность O(1)
def check_user_activate(lr, cu):
    if cu[2]:
        print(f'Доступ пользователю {lr} предоставлен')
        return True
    else:
        # запрос на активацию
        if str(input("Учетка не активирована. Выполнить активацию? (y/n)")) == 'y':
            cu[2] = True
            # Присвоение значения в словаре сложность O(1)
            user_dict[lr] = cu
            print(user_dict)
            print(f'Учетка для {lr} активирована')
            return True
        else:
            print(f'Учетка для {lr} не активирована. Доступ запрещен')
            return False


# Сложность O(1)
def check_user_access(login_r, password_r):
    access_accept = False
    c_user = check_user(login_r)
    if c_user is not None:
        if check_user_password(login_r, password_r, c_user[1]):
            check_user_activate(login_r, c_user)


user_dict = {'ID1': ['Ivanov', 'pass1', True],
             'ID2': ['Petrov', 'pass2', False],
             'ID3': ['Sidorov', 'pass3', True]}

login_request = str(input("ID (login): "))
password_request = str(input("Password: "))

check_user_access(login_request, password_request)

# Второе решение через списки не представлено
# если бы делал, поиск в списке будет со сложностью O(N log N), т.к. на сортировку именно на сортировкук уйдет это время

# Вариант поиска по словарю  будет быстрее, т.к. по сути при наличии ключа, словарь (hash table) просто возращает значение (сложность O(1))
