"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile
ent_num = 123456789
rev_num = 0


@profile()
def rev_1(enter_num, revers_num=0):
    num = enter_num % 10
    revers_num = (revers_num + num / 10) * 10
    enter_num //= 10
    return enter_num, revers_num


@profile()
def rev_2(enter_num, revers_num=0):
    num = enter_num % 10
    revers_num = (revers_num + num / 10) * 10
    enter_num //= 10
    return revers_num, enter_num


@profile()
def rev_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[-1]
    return enter_num, revers_num


def revers(enter_num, revers_num=0):
    num = 0
    if enter_num == 0:
        return int(revers_num + num / 10)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(revers(ent_num, rev_num))
print(revers_2(ent_num, rev_num))
print(revers_3(ent_num))



print(rev_1(ent_num, rev_num))
print(rev_2(ent_num, rev_num))
print(rev_3(ent_num))
