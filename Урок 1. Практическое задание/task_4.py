"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся:
- логин, 
- пароль 
- и отметка об активации учетной записи.

Нужно реализовать                       -- проверку, может ли пользователь быть допущен к ресурсу --
При этом его учетка должна быть         -- активирована --.
А если нет, то польз-лю                 -- нужно предложить ее пройти --.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.

"""
# вывод - 1 алгоритм эффективнее за счет наличия только одного цикла
user_massive = {
    'user_1':{'Login': 'User_1', 'Password':'HardPass_123', 'Activation':True},
    'user_2': {'Login': 'User_2', 'Password':'123_HardPass', 'Activation':False},
    'user_3': {'Login': 'User_3', 'Password':'123_Hp_321', 'Activation':False}
    }
user_input_1 = input('Введите учетные данныe: Логин и Пароль, через пробел ').split(' ')
def auth_user_func_1(main_dict, log_and_passw):   # общая сложность данного алгоритма О(n)
    list_at_item = list(main_dict.items()) # выделяем пользовталя / кортежи: "пользователь": "словарь данных"
    for i in list_at_item:
        user_dict = i[1] # выделям словарь
        if user_dict.get('Login') == log_and_passw[0]:
            if user_dict.get('Password') == log_and_passw[1] and user_dict.get('Activation') is True: 
                return 'Верный ввод учетных данных.\nПользователь активирован.\nДоступ предоставлен.'
            elif user_dict.get('Password') == log_and_passw[1] and user_dict.get('Activation') is False:
                return 'Верный ввод учетных данных.\nПользователь не активирован.\nПройдите процедуру активации.'
            elif user_dict.get('Password') != log_and_passw[1]:
                return 'Учетные данные введены не верно.\nВ доступе отказано.'
    return 'Не верно введен логин, или такого пользователя не сущесвтует.'

print(auth_user_func_1(user_massive, user_input_1))

def auth_user_func_2 (main_dict, log_and_passw): # общая сложность алгоритма О(n**2)
    list_at_item = list(main_dict.items())
    for i in list_at_item:
        val_list = list(i[1].values())
        if log_and_passw[0] in val_list:
            if log_and_passw[1] in val_list and True in val_list:                                   # дополнительный цикл
                return 'Верный ввод учетных данных.\nПользователь активирован.\nДоступ предоставлен'
            elif log_and_passw[1] in val_list and False in val_list:                                 # дополнительный цикл
                return 'Верный ввод учетных данных.\nПользователь не активирован.\nПройдите процедуру активации.'
            else:
                'Учетные данные введены не верно.\nВ доступе отказано.'
    return 'Данные введены не верно, или пользователя с таким логином - не сущесвтует'
    
counter_alg = input('Проверяем следующий алгоритм? - y/n ')
if counter_alg =='y':
    user_input_2 = input('Введите учетные данныe: Логин и Пароль, через пробел ').split(' ')
    print (auth_user_func_2 (user_massive, user_input_2))


