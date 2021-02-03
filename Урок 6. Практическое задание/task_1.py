"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

import timeit
import psutil
from memory_profiler import profile
from timeit import timeit
from random import randrange
from random import randint
import hashlib
from sys import getrefcount

# 1


@profile
def my_func_gen(u_inp):
    """формирует список чисел из указываемой длинны списка"""
    sys_list = [i for i in range(u_inp+1)]
    return sys_list


@profile
def my_func(u_inp):
    sys_list = []
    u_list = range(u_inp+1)
    for i in u_list:
        sys_list.append(i)
    return sys_list


my_func_gen(1000)
my_func(1000)

# 2

@profile
def authentication_1():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    password_hash = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    with open('hash_password.txt', 'w', encoding='utf-8') as f1:
        f1.write(password_hash)
    repeat_password = \
        input('Пожалуйста введите пароль ещё раз: ')
    repeat_password_hash = \
        hashlib.sha256(login.encode('utf-8') + repeat_password.encode('utf-8')).hexdigest()
    with open('hash_password.txt', 'r', encoding='utf-8') as f2:
        if f2.read() == repeat_password_hash:
            return 'Доступ предоставлен'
        else:
            return 'В доступе отказано'


authentication_1()
user_pass = input('Введите свой пароль: ')


@profile
def authentication_2(user_input, sys_paswd='123'):
    hash_user_input = hashlib.sha256(user_input.encode('utf-8')).hexdigest()
    if user_input == sys_paswd:
        user_input = input(f'1-ая проверка успешна. \
        \nВ базе данных записана строка:\
        \n{hash_user_input}\nДля завершения проверки\
        \nВведите ваш пароль повторно: ')
        hash_checkout_user_input = \
            hashlib.sha256(user_input.encode('utf-8')).hexdigest()
        if hash_checkout_user_input == hash_user_input:
            print('Вы ввели верный пароль. Доступ предоставлен')
        else:
            u_inp = input('Пароли не совпадают. В доступе отказано\
            \nПроцедура проверки начнется заново.\
            \nВведите свой пароль ')
            return authentication_2(u_inp, sys_paswd)
        return
    else:
        u_inp = input('Пароли не совпадают. В доступе отказано\
        \nПроцедура проверки начнется заново.\
        \nВведите свой пароль ')
        return authentication_2(u_inp, sys_paswd)


authentication_2(user_pass)


# 3
@profile
def my_func_gen_2():
    """вывод больших значений по сравнению с предыдущим"""
    a = [randint(1, 100) for _ in range(1000)]
    res = [a[i] for i in range(1, len(a)) if a[i - 1] < a[i]]
    print(getrefcount(a))
    del a
    print(getrefcount(res))
    return res


@profile
def my_func_while():
    b = [randint(1, 100) for _ in range(1000)]
    i = 0
    new_list = []
    while i < len(b):
        if b[i - 1] < b[i]:
            new_list.append(b[i])
        i += 1
    print(getrefcount(b))
    del b
    print(getrefcount(new_list))
    return new_list

my_func_gen_2()
my_func_while()


"""
при выполнении
# my_func_gen(1000):
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    26     17.6 MiB     17.6 MiB           1   @profile
    27                                         def my_func_gen(u_inp):
    28     17.6 MiB      0.0 MiB        1004       sys_list = [i for i in range(u_inp+1)]
    29     17.6 MiB      0.0 MiB           1       return sys_list

 my_func(1000)
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32     17.6 MiB     17.6 MiB           1   @profile
    33                                         def my_func_rec(u_inp):
    34     17.6 MiB      0.0 MiB           1       sys_list = []
    35     17.6 MiB      0.0 MiB           1       u_list = range(u_inp+1)
    36     17.6 MiB      0.0 MiB        1002       for i in u_list:
    37     17.6 MiB      0.0 MiB        1001           sys_list.append(i)
    38     17.6 MiB      0.0 MiB           1       return sys_list

authentication_1
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     17.8 MiB     17.8 MiB           1   @profile
    46                                         def authentication_1():
    47     17.8 MiB      0.0 MiB           1       login = input('Введите логин: ')
    48     17.8 MiB      0.0 MiB           1       password = input('Введите пароль: ')
    49     17.8 MiB      0.0 MiB           1       password_hash = hashlib.sha256(login.encode('utf-8') + password.encode('utf-8')).hexdigest()
    50     17.8 MiB      0.0 MiB           1       with open('hash_password.txt', 'w', encoding='utf-8') as f1:
    51     17.8 MiB      0.0 MiB           1           f1.write(password_hash)
    52     17.8 MiB      0.0 MiB           1       repeat_password = input('Пожалуйста введите пароль ещё раз: ')
    53     17.8 MiB      0.0 MiB           1       repeat_password_hash = hashlib.sha256(login.encode('utf-8') + repeat_password.encode('utf-8')).hexdigest()
    54     17.8 MiB      0.0 MiB           1       with open('hash_password.txt', 'r', encoding='utf-8') as f2:
    55     17.8 MiB      0.0 MiB           1           if f2.read() == repeat_password_hash:
    56     17.8 MiB      0.0 MiB           1               return 'Доступ предоставлен'
    57                                                 else:
    58                                                     return 'В доступе отказано'

authentication_2
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    65     17.8 MiB     17.8 MiB           1   @profile
    66                                         def authentication_2(user_input, sys_paswd='123'):
    67     17.8 MiB      0.0 MiB           1       hash_user_input = hashlib.sha256(user_input.encode('utf-8')).hexdigest()
    68     17.8 MiB      0.0 MiB           1       if user_input == sys_paswd:
    69     17.8 MiB      0.0 MiB           2           user_input = input(f'1-ая проверка успешна. \
    70                                                 \nВ базе данных записана строка:\
    71     17.8 MiB      0.0 MiB           1           \n{hash_user_input}\nДля завершения проверки\
    72                                                 \nВведите ваш пароль повторно: ')
    73     17.8 MiB      0.0 MiB           1           hash_checkout_user_input = \
    74     17.8 MiB      0.0 MiB           1               hashlib.sha256(user_input.encode('utf-8')).hexdigest()
    75     17.8 MiB      0.0 MiB           1           if hash_checkout_user_input == hash_user_input:
    76     17.8 MiB      0.0 MiB           1               print('Вы ввели верный пароль. Доступ предоставлен')
    77                                                 else:
    78                                                     u_inp = input('Пароли не совпадают. В доступе отказано\
    79                                                     \nПроцедура проверки начнется заново.\
    80                                                     \nВведите свой пароль ')
    81                                                     return authentication(u_inp, sys_paswd)
    82     17.8 MiB      0.0 MiB           1           return
    83                                             else:
    84                                                 u_inp = input('Пароли не совпадают. В доступе отказано\
    85                                                 \nПроцедура проверки начнется заново.\
    86                                                 \nВведите свой пароль ')
    87                                                 return authentication(u_inp, sys_paswd)

для сравнения взял простейший итератор + 
сложный скрипт, где задействованы: работа с файлами
и рекурсия

В результате - затраты памети практически идентичны в случае с выполнением 
одной строки кода
однако суммарное определение по скрипту больше
Замечу (возможно очевидное), что в случаях с услвоиями (if - else)
память выделяется на рабочее услвоие, а в том случае,
если условие в коде не срабатывает python его пропускает


наибольшее кол-во памяти в простом скрипте затрачено при использовании 
функ append и выдлении пустого списка в качесвте переменной. Сюда уходит память,
которую экономит итератор 

Наибольшое кол-во памяти в более сложном скрипте 
затарчено при использовании authentication_1,
из-за четко-определнного алгоритма скрипта (нет if-else)
но рекурсия срабатывает с меньшим ресурсом лишь потому, что 
пользовательский ввод был введен верно с первой попытки, в противном случае
ресурсы памяти распределялись бы иначе:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    67     17.8 MiB     17.8 MiB           3   @profile
    68                                         def authentication_2(user_input, sys_paswd='123'):
    69     17.8 MiB      0.0 MiB           3       hash_user_input = hashlib.sha256(user_input.encode('utf-8')).hexdigest()
    70     17.8 MiB      0.0 MiB           3       if user_input == sys_paswd:
    71     17.8 MiB      0.0 MiB           4           user_input = input(f'1-ая проверка успешна. \
    72                                                 \nВ базе данных записана строка:\
    73     17.8 MiB      0.0 MiB           2           \n{hash_user_input}\nДля завершения проверки\
    74                                                 \nВведите ваш пароль повторно: ')
    75     17.8 MiB      0.0 MiB           2           hash_checkout_user_input = \
    76     17.8 MiB      0.0 MiB           2               hashlib.sha256(user_input.encode('utf-8')).hexdigest()
    77     17.8 MiB      0.0 MiB           2           if hash_checkout_user_input == hash_user_input:
    78     17.8 MiB      0.0 MiB           1               print('Вы ввели верный пароль. Доступ предоставлен')
    79                                                 else:
    80     17.8 MiB      0.0 MiB           1               u_inp = input('Пароли не совпадают. В доступе отказано\
    81                                                     \nПроцедура проверки начнется заново.\
    82                                                     \nВведите свой пароль ')
    83     17.8 MiB      0.0 MiB           1               return authentication_2(u_inp, sys_paswd)
    84     17.8 MiB      0.0 MiB           1           return
    85                                             else:
    86     17.8 MiB      0.0 MiB           1           u_inp = input('Пароли не совпадают. В доступе отказано\
    87                                                 \nПроцедура проверки начнется заново.\
    88                                                 \nВведите свой пароль ')
    89     17.8 MiB      0.0 MiB           1           return authentication_2(u_inp, sys_paswd)

как видно из profile - при рекурсии и действии всех возможных вариантов условий
такой случай будет более ресурсозатратным

# 3
my_func_gen_2
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   102     17.8 MiB     17.8 MiB           1   @profile
   103                                         def my_func_gen_2():
   104                                             
   105     17.8 MiB      0.0 MiB        1003       a = [randint(1, 100) for _ in range(1000)]
   106     17.8 MiB      0.0 MiB        1002       res = [a[i] for i in range(1, len(a)) if a[i - 1] < a[i]]
   107     17.8 MiB      0.0 MiB           1       print(getrefcount(a))
   108     17.8 MiB      0.0 MiB           1       del a
   109     17.8 MiB      0.0 MiB           1       print(getrefcount(res))
   110     17.8 MiB      0.0 MiB           1       return res


my_func_while
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   113     17.8 MiB     17.8 MiB           1   @profile
   114                                         def my_func_while():
   115     17.8 MiB      0.0 MiB        1003       b = [randint(1, 100) for _ in range(1000)]
   116     17.8 MiB      0.0 MiB           1       i = 0
   117     17.8 MiB      0.0 MiB           1       new_list = []
   118     17.8 MiB      0.0 MiB        1001       while i < len(b):
   119     17.8 MiB      0.0 MiB        1000           if b[i - 1] < b[i]:
   120     17.8 MiB      0.0 MiB         492               new_list.append(b[i])
   121     17.8 MiB      0.0 MiB        1000           i += 1
   122     17.8 MiB      0.0 MiB           1       print(getrefcount(b))
   123     17.8 MiB      0.0 MiB           1       del b
   124     17.8 MiB      0.0 MiB           1       print(getrefcount(new_list))
   125     17.8 MiB      0.0 MiB           1       return new_list


в третьем скрипте явное преимущесвто итератора по сравнению с циклом while
это связано из-за большого кол-ва проверок и рассчетов элементов индекса в каждую итерацию цикла
+
использования встренных функций (append) для добавления в пустой список, также потребляющий память


python 3.8.7
ОС - Linux mint 20.01 64х
"""