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
db = []

db.append({'login': 'user1', 'pass': 'pass1', 'act_ind': 'Y'})
db.append({'login': 'user2', 'pass': 'pass2', 'act_ind': 'N'})
db.append({'login': 'user3', 'pass': 'pass3', 'act_ind': 'Y'})
db.append({'login': 'user4', 'pass': 'pass4', 'act_ind': 'Y'})
db.append({'login': 'user5', 'pass': 'pass5', 'act_ind': 'Y'})

def binary_search(i_lst, i_log):
    start = 0
    end = len(i_lst) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if i_lst[mid]['login'] == i_log:
            return i_lst[mid]
        elif i_lst[mid]['login'] < i_log:
            start = mid + 1
        else:
            end = mid - 1
    return None

def liner_search(i_lst, i_log):
    for rec in i_lst:
        if rec['login'] == i_log:
            return rec

    return None

def access_basic_logic(i_user, i_pass):
    if not i_user:
        print('Логин/пароль некорректны!')
        return False

    if i_user['pass'] != i_pass:
        print('Логин/пароль некорректны!')
        return False

    if i_user['act_ind'] == 'Y':
        print('Доступ предоставлен!')
        return True

    act_list = ['стол', 'шкаф', 'кошка', 'табурет', 'кровать']

    odd_word = input(f'Активация учетной записи.\nВведите лишнее слово(с учетом регистра){act_list}:')

    if odd_word == 'кошка':
        i_user['act_ind'] = 'Y'
        print('Активация учетной записи успешно пройдена!\nДоступ предоставлен!')
        return True
    else:
        print('Активация учетной записи не пройдена!')

    return False

def is_access_permitted_1(i_login, i_pass, i_db):
    l_user = binary_search(i_db, i_login)

    return access_basic_logic(l_user, i_pass)

def is_access_permitted_2(i_login, i_pass, i_db):
    l_user = liner_search(i_db, i_login)

    return access_basic_logic(l_user, i_pass)

print(db)
#print(is_access_permitted_1('user2', 'pass2', db))
print(is_access_permitted_2('user2', 'pass2', db))
##################################################
# Решение 1 - функция is_access_permitted_1.
# Сложность алгоритма: (nlog n) - логарифмическая.
# Поиск пользователя осуществляется методом двоичного поиска в отсортированном списке.
#
# Решение 2 - функция is_access_permitted_2.
# Сложность алгоритма: O(n) - линейная.
# Поиск пользователя осуществляется перебором элементов списка.
#
# Вывод: первое решение эффективней, потому, что:
# логарифмическая сложность эффективней линейной.
##################################################

