"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

from hashlib import md5


def user_str():
    user_input = input('Your string, or [q] to exit: ')
    if user_input == 'q':
        return 'Fin.'
    else:
        return user_str_count(user_input)


def user_str_count(user_input):
    res_list = []
    for i in range(1, len(user_input) + 1):
        for n in range(0, i):
            el = md5(user_input[n:i].encode()).hexdigest()
            res_list.append(el)
    res_list_to_set = set(res_list)
    print(f'Substring count in "{user_input}" - {len(res_list_to_set) - 1}')
    return user_str()


user_str()

# GB method
# видимо, не понял задания

s = input('Enter your string: ')
r = set()

N = len(s)
for i in range(N):
    if i == 0:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range (N, i , -1):
        print(s[i:j])
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print(r)
