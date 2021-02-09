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

substr_set = set()
print('Input string:')
v_str = input()
for s_start in range(len(v_str)):
    if s_start == 0: str_limit = len(v_str)
    else: str_limit = len(v_str)+1
    for s_end in range(s_start+1, str_limit):
        substr_set.add( hash(v_str[s_start:s_end]) )

print(str(len(substr_set)))
print(substr_set)