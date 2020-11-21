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


import hashlib


print('Program "Count all substrings of input string"')
input_str = input('Please enter a string with small little letters: ')
final_set = set()
try:
    len_inpt_str = len(input_str)
    for el in range(len_inpt_str):
        if el == 0:
            len_inpt_str = len(input_str) - 1
        else:
            len_inpt_str = len(input_str)
        for el2 in range(len_inpt_str, el, -1):
            print(input_str[el:el2])
            final_set.add(hashlib.sha1(input_str[el:el2].encode('utf-8')).hexdigest())
except ValueError:
    print('Error! Value error!')
except:
    print('Error! Unknown error!')

print(f'Count substrings in string "{input_str}" is {len(final_set)}')
print(f'Final set is : {final_set}')