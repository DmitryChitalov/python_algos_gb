"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
# Версия 3.8 64
import hashlib
from memory_profiler import profile
import random


@profile
def prog1():
    my_string = input('Введите строку, состоящую только из маленьких латинских букв: ')
    sum_substring = set()

    for i in range(len(my_string)):
        for j in range(len(my_string), i, -1):
            hash_str = hashlib.sha1(my_string[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)

    return print(f'{len(sum_substring) - 1} различных подстрок в строке {my_string}')


@profile
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@profile
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


@profile
def wrapper():
    num = int(input('Введите число: '))

    def revers(enter_num, revers_num=0):
        if enter_num == 0:
            return
        else:
            num = enter_num % 10
            revers_num = (revers_num + num / 10) * 10
            enter_num //= 10
            revers(enter_num, revers_num)

    return revers(num)

@profile
def play():
    cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
    random.shuffle(cards)
    count = 0
    print('Играем в 21 очко')

    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            current = cards.pop()
            print('Вам попалась карта достоинством %d' % current)
            count += current
            if count > 21:
                print('Извините, но вы проиграли')
                break
            elif count == 21:
                print('Поздравляю, вы набрали 21!')
                break
            else:
                print('У вас %d очков.' % count)
        elif choice == 'n':
            print('У вас %d очков и вы закончили игру.' % count)
            break


revers_2(1234)
revers_3(1234)
wrapper()
prog1()
play()

"""Возможно, это какие-то неудачные примеры, никакой аналитики невозможно провести, тк везде
нулевое использование ресурсов памяти. В целом, тема мне понятна, так что ,наверно, это не критично.
Лучше было бы работать с готовыми , заведомо интересными примерами"""