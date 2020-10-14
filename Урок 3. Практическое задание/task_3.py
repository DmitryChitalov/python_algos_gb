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
р                     S[i:j:step]
а
"""
import hashlib

def fun():
    s = 'papa'
    set_variations = set()
    N = len(s)
    for i in range(N):
        if i==0:
            N=len(s)-1
        else:
            N=len(s)
            for j in range(N, i,-1):
                #print(s[i:j])
                set_variations.add(hashlib.md5(s[i:j].encode()).hexdigest())
    print(f'Всего {len(set_variations)+1} вариаций')

print(fun());