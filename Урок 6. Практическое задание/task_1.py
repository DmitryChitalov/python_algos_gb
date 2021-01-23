"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import sys
from random import randint
from pympler import asizeof
from time import process_time
from memory_profiler import profile
from memory_profiler import memory_usage

""" Функция поиска минимума путем прохода по списку и сравнения каждого элемента с 
    встречающимся до этого элементом списка и имеющим минимальное значение на текущий момент"""


@profile                                # декоратор профилировки ф-ии по памяти
def search_min_1(gen):
    start_list = list(gen)                  # >>> list comprehension
    list_min_el = [start_list.pop(0)]       # >>> извлечение первого элемента и помещение его в новый список
    # asizeof.asizeof(start_list)             # 4077176 - размер списка, полученного из генератора
    # asizeof.asizeof(gen)                    # 112 - размер генератора уменьшился
    for el in start_list:               # перебор списка
        if el < list_min_el[-1]:        # сравнение с последним добавленным значением в новый список
            list_min_el.append(el)
    min_el = list_min_el[-1]
    del start_list                      # >>> удаление списка
    return min_el                       # возвращение минимального числа


""" Функция поиска минимума путем извлечения последнего элемента списка, отсортированного с помощью
    алгоритма быстрой сортировки """


@profile                                # декоратор профилировки ф-ии по памяти
def search_min_2(gen):
    start_list = list(gen)                  # >>> создание списка
    sorted_list = quicksort(start_list)     # >>> выполнение рек-й ф-ии и получение нового списка
    # asizeof.asizeof(start_list)             # 4077176
    # asizeof.asizeof(gen)                    # 112 - размер генератора уменьшился
    min_el = sorted_list[0]
    del start_list                      # >>> удаление списка
    del sorted_list                     # >>> удаление отсортированного списка
    return min_el                       # возвращение минимального числа


def quicksort(lst):
    length = len(lst)                       # длина полученного списка
    middle = length // 2                    # индекс серединного элемента (опорного элемента)
    if length < 2:                          # условие завершения рекурсии
        return lst
    pivot = lst[middle]                     # опорный элемент
    left = [i for i in lst if i < pivot]    # список элементов меньше опорного
    right = [i for i in lst if i > pivot]   # ... больше опорного
    return quicksort(left) + [pivot] + quicksort(right)     # рекурсивный вызов с разветвлениями


""" 
Программа, которая принимает на вход список игр футбольных команд с результатом матча и 
выводит сводную таблицу результатов всех матчей.

Результаты игры в следующем формате: 
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
"""


def scoreboard(table):
    input_table = [team.split(';') for row in table for team in row]

    numbers = set(str(i) for i in range(100))

    n_games_team = {team: 0 for row in input_table for team in row if team not in numbers}
    n_win_team = {team: 0 for row in input_table for team in row if team not in numbers}
    n_draw_team = {team: 0 for row in input_table for team in row if team not in numbers}
    n_lose_team = {team: 0 for row in input_table for team in row if team not in numbers}
    all_points = {team: 0 for row in input_table for team in row if team not in numbers}

    for row in input_table:
        for team in row:
            if team in n_games_team:
                n_games_team[team] += 1

    for row in input_table:
        if int(row[1]) > int(row[3]):
            n_win_team[row[0]] += 1
            n_lose_team[row[2]] += 1
            all_points[row[0]] += 3
        if int(row[1]) < int(row[3]):
            n_win_team[row[2]] += 1
            n_lose_team[row[0]] += 1
            all_points[row[2]] += 3
        if int(row[1]) == int(row[3]):
            n_draw_team[row[0]] += 1
            n_draw_team[row[2]] += 1
            all_points[row[0]] += 1
            all_points[row[2]] += 1

    for team, games in n_games_team.items():
        print('{:>9}: {} {} {} {} {}'.format(team, games, n_win_team[team], n_draw_team[team], n_lose_team[team],
                                             all_points[team]))


if __name__ == '__main__':
    """ Запуск 1 и 2 функций"""
    gen_1 = (randint(11, 100000) for _ in range(100000))
    gen_2 = (randint(11, 100000) for _ in range(100000))

    asizeof.asizeof(gen_1)          # 432 - размер генератора
    asizeof.asizeof(gen_2)          # 432

    time_search_min_1 = process_time()      # замеры времени
    search_min_1(gen_1)
    print('Результаты: Изначально выделенная память для выполнения программы составила 31.9 MiB\n'
          'Для преобразования генератора в список дополнитально выделенная память составила 4.7 MiB\n'
          'Перед завершением программы созданный список был удален, и с этим освободилось 4.3 MiB\n'
          'На выходе из программы показатель выделенной памяти остановился на значении 32.3 MiB\n')

    time_off_1 = process_time()             # замеры времени

    search_min_2(gen_2)
    print('Результаты: Изначально выделенная память для выполнения программы составила 31.9 MiB\n'
          'Для преобразования генератора в список дополнитально выделенная память составила 4.7 MiB\n'
          'Затем с помощью рекурсивной функций был создан новый список. Выделенная память: 0.7 MiB\n'
          'Перед завершением программы созданные списки были удалены, и с этим освободилось 4 MiB\n'
          'На выходе из программы показатель выделенной памяти остановился на значении 33.2 MiB\n')
    print('-'*100)
    print('Вывод: Функция search_min_1 использует память более эффективно, так как в данной функции\n'
          'дополнительный список не является полной копией (отсортированной) списка start_list. В таком случае\n'
          'для содержания дополнительного списка программе хватает стандартной выделенной памяти (Increment=0)\n'
          'Для уравнивания эффективности использования памяти была добавлена ф-ия del.\n'
          'Данная ф-ия производит удаление списков (ярлыков), освобождая память, но на выходе у функции search_min_1 \n'
          'используемая память все равно остается меньше, чем в search_min_2. Возможно это связано с \n'
          'использованием рекурсии во второй функции.\n'
          '\n'
          'Преимуществом 2й функции является время выполнения\n')

    time_off_2 = process_time()                     # рассчеты времени
    time_diff_1 = time_off_1 - time_search_min_1
    time_diff_2 = time_off_2 - time_off_1

    print(f'Выполнение 1й функции заняло: {time_diff_1} сек.\n'
          f'Выполнение 2й функции заняло: {time_diff_2} сек.\n')

    """Запуск 3й функции """
    list_games = [['Спартак;9;Зенит;10'],
                  ['Локомотив;12;Зенит;3'],
                  ['Спартак;8;Локомотив;15']]

    # левые отсечки времени и памяти
    t1 = process_time()
    m1 = memory_usage()

    scoreboard(list_games)

    # правые отсечки времени и памяти
    t2 = process_time()
    m2 = memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f'\nВремя выполнения составило: {time_diff} сек and {mem_diff} Mib памяти')

    """
    Результаты: Время выполнения составило: 0.0 сек and 0.01171875 MiB памяти

    Вывод: Данная функция не принимает на вход большое кол-во данных, поэтому время выполнения и выделяемая память
    не нуждаются в оптимизации.
    """

version = sys.version       # версия Python и разрядность ОС
                            # 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
