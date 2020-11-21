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

from memory_profiler import profile
from random import random, shuffle
from time import time
from random import randint


# 1)
# Функции из урока №1, задания №4:

def number_1():
    # nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [randint(1, 10) for i in range(300)]

    @profile
    def func_1(nums):
        new_arr = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                new_arr.append(i)
        return new_arr

    def memorize(func):
        def wrapper(nums, new_set=set(), i=0, memory={}):
            result = memory.get(i)
            if result == None:
                result = func(nums, new_set, i)
                memory[i] = result
            return result

        return wrapper

    @memorize
    def func_2(nums, new_set=set(), i=0):
        if i != len(nums):
            if nums[i] % 2 == 0:
                new_set.add(nums.index(nums[i]))
            return func_2(nums, new_set, i + 1)
        else:
            return new_set

    # добавлена обёртка для профайлера:
    @profile
    def profiled_rec_func(f):
        def wrapper(nums, new_set=set(), i=0):
            return f(nums, new_set, i + 1)

        return wrapper

    func_1(nums)
    profiled_rec_func(func_2(nums))


'''
Вывод профайлера:

Filename: */task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     17.4 MiB     17.4 MiB           1   @profile
    30                                         def func_1(nums):
    31     17.4 MiB      0.0 MiB           1       new_arr = []
    32     17.4 MiB      0.0 MiB         301       for i in range(len(nums)):
    33     17.4 MiB      0.0 MiB         300           if nums[i] % 2 == 0:
    34     17.4 MiB      0.0 MiB         154               new_arr.append(i)
    35     17.4 MiB      0.0 MiB           1       return new_arr


Filename: */task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    59     17.9 MiB     17.9 MiB           1   @profile
    60                                         def profiled_rec_func(f):
    61     17.9 MiB      0.0 MiB           1       def wrapper(nums, new_set=set(), i=0):
    62                                                 return f(nums, new_set, i + 1)
    63     17.9 MiB      0.0 MiB           1       return wrapper



Process finished with exit code 0


Наблюдения и выводы:
в процессе выполнения обоих версий алгоритмов (цикл и рекурсия с мемоизацией) прироста
занятой памяти не наблюдается, но видно, что цикл занимает меньше памяти, чем рекурсия.
'''


# 2)
# Функции из урока №4, задания №4:

def number_2():
    array = [1, 3, 1, 3, 4, 5, 1]
    array = [randint(1, 9) for i in range(200)]

    @profile
    def func_1():
        m = 0
        num = 0
        for i in array:
            count = array.count(i)
            if count > m:
                m = count
                num = i
        return f'Чаще всего встречается число {num}, ' \
               f'оно появилось в массиве {m} раз(а)'

    @profile
    def func_2():
        new_array = []
        for el in array:
            count2 = array.count(el)
            new_array.append(count2)

        max_2 = max(new_array)
        elem = array[new_array.index(max_2)]
        return f'Чаще всего встречается число {elem}, ' \
               f'оно появилось в массиве {max_2} раз(а)'

    # Третий, оптимизированный с помощью мемоизации, алгоритм:

    def memorize(func):
        def wrapper(i=0, mem={}):
            result = mem.get(i)
            if result is None:
                result = func(i)
                mem[i] = result
            return result

        return wrapper

    @memorize
    def func_3(i=0, nums_dict={}):
        if i < len(array):
            if nums_dict.get(array[i]) is None:
                nums_dict[array[i]] = 1
            else:
                nums_dict[array[i]] += 1
            return func_3(i + 1)
        else:
            max_count, max_num = 0, 0
            for k in nums_dict.keys():
                if nums_dict[k] > max_count:
                    max_count = nums_dict[k]
                    max_num = k
            return f'Чаще всего встречается число {max_num}, ' \
                   f'оно появилось в массиве {max_count} раз(а)'

    # добавлена обёртка для профайлера:
    @profile
    def profiled_rec_func(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    func_1()
    func_2()
    profiled_rec_func(func_3())


'''
Вывод профайлера:

Filename: */task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   112     17.5 MiB     17.5 MiB           1       @profile
   113                                             def func_1():
   114     17.5 MiB      0.0 MiB           1           m = 0
   115     17.5 MiB      0.0 MiB           1           num = 0
   116     17.5 MiB      0.0 MiB           8           for i in array:
   117     17.5 MiB      0.0 MiB           7               count = array.count(i)
   118     17.5 MiB      0.0 MiB           7               if count > m:
   119     17.5 MiB      0.0 MiB           1                   m = count
   120     17.5 MiB      0.0 MiB           1                   num = i
   121     17.5 MiB      0.0 MiB           1           return f'Чаще всего встречается число {num}, ' \
   122                                                        f'оно появилось в массиве {m} раз(а)'


Filename: */task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   124     17.5 MiB     17.5 MiB           1       @profile
   125                                             def func_2():
   126     17.5 MiB      0.0 MiB           1           new_array = []
   127     17.5 MiB      0.0 MiB           8           for el in array:
   128     17.5 MiB      0.0 MiB           7               count2 = array.count(el)
   129     17.5 MiB      0.0 MiB           7               new_array.append(count2)
   130                                         
   131     17.5 MiB      0.0 MiB           1           max_2 = max(new_array)
   132     17.5 MiB      0.0 MiB           1           elem = array[new_array.index(max_2)]
   133     17.5 MiB      0.0 MiB           1           return f'Чаще всего встречается число {elem}, ' \
   134                                                        f'оно появилось в массиве {max_2} раз(а)'


Filename: */task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   166     17.5 MiB     17.5 MiB           1       @profile
   167                                             def profiled_rec_func(f):
   168     17.5 MiB      0.0 MiB           1           def wrapper(*args, **kwargs):
   169                                                     return f(*args, **kwargs)
   170                                         
   171     17.5 MiB      0.0 MiB           1           return wrapper



Process finished with exit code 0


Наблюдения и выводы:
Функция с рекурсией с мемоизацией занимает совсем немного больше памяти, чем функция с циклом
в данной ситуации. Я думаю, что это связано с необходимостью перебрать весь массив чисел.
'''


# 3)
# Игра "Лото" в консоли, предложенная к написанию вместо последнего д/з на курсе основ Python.

def number_3():
    # функция для декоратора замера времени:
    def time_count(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            out = func(*args, **kwargs)
            end_time = time()
            print(f'Время выполнения {func}: {end_time - start_time} секунд.')
            return out

        return wrapper

    rolled = []
    number_of_kegs = 90

    class Gamer:
        def __init__(self):

            self.nums_per_line = 5
            self.player_card = [['----------Gamer-----------'], ['   ', '   ', '   ', '   '],
                                ['   ', '   ', '   ', '   '],
                                ['   ', '   ', '   ', '   '], ['--------------------------']]

        # @time_count
        @profile
        def __str__(self):
            [[print(j, end='') for j in i] and print() for i in self.player_card]
            return ''

        # @time_count
        @profile
        def roll(self):
            yield round(random() * (90 - 1) + 1)

        # @time_count
        @profile
        def give_me_num(self):
            for self.__el in self.roll():
                return self.__el

        # @time_count
        @profile
        def fill_card(self):
            self.__card_num = self.give_me_num()
            self._total_in_card = []
            for line in range(len(self.player_card) - 2):
                self.__needed = []
                for i in range(self.nums_per_line):
                    while self.__card_num in self._total_in_card:
                        for el in self.roll():
                            self.__card_num = el
                    if self.__card_num < 10:
                        self.__card_num = ' ' + str(self.__card_num)
                    self.__needed.append(str(self.__card_num) + ' ')
                    self._total_in_card.append(self.__card_num)

                self.player_card[line + 1].extend(self.__needed)
                shuffle(self.player_card[line + 1])

        # @time_count
        @profile
        def step(self, current_num):
            self._found = False
            self.__current_num = current_num
            self.user_answer = input('Зачеркнуть? (у/n): ').lower()
            if self.__current_num == 0:
                print('Бочонков больше не осталось!')
                return False
            for i in range(1, len(self.player_card)):
                for j in self.player_card[i]:
                    if str(self.__current_num) in j:
                        if self.__current_num < 10 and len(j.rstrip().lstrip()) == 1 or \
                                (self.__current_num >= 10 and len(j.rstrip()) == 2):
                            self._found = True
                            if self.user_answer == 'y':
                                self.player_card[i][self.player_card[i].index(j)] = '-- '
                                if self.__current_num < 10:
                                    del self._total_in_card[
                                        self._total_in_card.index(' ' + str(self.__current_num))]
                                    break
                                elif self.__current_num >= 10:
                                    del self._total_in_card[
                                        self._total_in_card.index(self.__current_num)]
                                    break

            if (self.user_answer == 'n' and self._found == True) or (self.user_answer == 'y' and self._found == False):
                print('Вы проиграли!')
                return False

        # @time_count
        @profile
        def check_win(self):
            if len(self._total_in_card) == 0:
                return True

    class Player(Gamer):
        def __init__(self):
            super().__init__()
            self.player_card[0] = ['----------Player----------']

        # @time_count
        @profile
        def num_from_bag(self):
            self._num = self.give_me_num()
            if len(rolled) >= 90:
                return 0

            while self._num in rolled:
                self._num = self.give_me_num()
            rolled.append(self._num)
            return self._num

    class Computer(Gamer):
        def __init__(self):
            super().__init__()
            self.player_card[0] = ['---------Computer---------']

        # @time_count
        @profile
        def step(self, current_num):
            self.__current_num = current_num
            for i in range(1, len(self.player_card)):
                for j in self.player_card[i]:
                    if str(self.__current_num) in j:
                        if self.__current_num < 10 and len(j.rstrip().lstrip()) == 1:
                            self.player_card[i][self.player_card[i].index(j)] = '-- '
                            del self._total_in_card[
                                self._total_in_card.index(' ' + str(self.__current_num))]
                        elif self.__current_num >= 10 and len(j.rstrip()) == 2:
                            self.player_card[i][self.player_card[i].index(j)] = '-- '
                            del self._total_in_card[
                                self._total_in_card.index(self.__current_num)]
                        break

    a = Player()
    b = Computer()
    a.fill_card()
    b.fill_card()


    @profile
    def play_game():
        while len(rolled) <= number_of_kegs:
            print(a, end='')
            print('==========================')
            print(b)

            keg = a.num_from_bag()
            print(f'Выпал бочонок с номером {keg}')

            if a.step(keg) == False:
                break
            elif a.check_win() == True:
                print('Игрок победил!')
                break
            elif b.check_win() == True:
                print('Компьютер победил!')
                break
            b.step(keg)

    play_game()


'''
Вывод программы и профайлера:

Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     17.3 MiB     17.3 MiB           1       @profile
    43                                             def give_me_num(self):
    44     17.3 MiB      0.0 MiB           1           for self.__el in self.roll():
    45     17.3 MiB      0.0 MiB           1               return self.__el


Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    47     17.3 MiB     17.3 MiB           1       @profile
    48                                             def fill_card(self):
    49     17.3 MiB      0.0 MiB           1           self.__card_num = self.give_me_num()
    50     17.3 MiB      0.0 MiB           1           self._total_in_card = []
    51     17.3 MiB      0.0 MiB           4           for line in range(len(self.player_card) - 2):
    52     17.3 MiB      0.0 MiB           3               self.__needed = []
    53     17.3 MiB      0.0 MiB          18               for i in range(self.nums_per_line):
    54     17.3 MiB      0.0 MiB          30                   while self.__card_num in self._total_in_card:
    55     17.3 MiB      0.0 MiB          30                       for el in self.roll():
    56     17.3 MiB      0.0 MiB          15                           self.__card_num = el
    57     17.3 MiB      0.0 MiB          15                   if self.__card_num < 10:
    58     17.3 MiB      0.0 MiB           1                       self.__card_num = ' ' + str(self.__card_num)
    59     17.3 MiB      0.0 MiB          15                   self.__needed.append(str(self.__card_num) + ' ')
    60     17.3 MiB      0.0 MiB          15                   self._total_in_card.append(self.__card_num)
    61                                         
    62     17.3 MiB      0.0 MiB           3               self.player_card[line + 1].extend(self.__needed)
    63     17.3 MiB      0.0 MiB           3               shuffle(self.player_card[line + 1])


Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     17.3 MiB     17.3 MiB           1       @profile
    43                                             def give_me_num(self):
    44     17.3 MiB      0.0 MiB           1           for self.__el in self.roll():
    45     17.3 MiB      0.0 MiB           1               return self.__el


Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    47     17.3 MiB     17.3 MiB           1       @profile
    48                                             def fill_card(self):
    49     17.3 MiB      0.0 MiB           1           self.__card_num = self.give_me_num()
    50     17.3 MiB      0.0 MiB           1           self._total_in_card = []
    51     17.3 MiB      0.0 MiB           4           for line in range(len(self.player_card) - 2):
    52     17.3 MiB      0.0 MiB           3               self.__needed = []
    53     17.3 MiB      0.0 MiB          18               for i in range(self.nums_per_line):
    54     17.3 MiB      0.0 MiB          29                   while self.__card_num in self._total_in_card:
    55     17.3 MiB      0.0 MiB          28                       for el in self.roll():
    56     17.3 MiB      0.0 MiB          14                           self.__card_num = el
    57     17.3 MiB      0.0 MiB          15                   if self.__card_num < 10:
    58     17.3 MiB      0.0 MiB           3                       self.__card_num = ' ' + str(self.__card_num)
    59     17.3 MiB      0.0 MiB          15                   self.__needed.append(str(self.__card_num) + ' ')
    60     17.3 MiB      0.0 MiB          15                   self._total_in_card.append(self.__card_num)
    61                                         
    62     17.3 MiB      0.0 MiB           3               self.player_card[line + 1].extend(self.__needed)
    63     17.3 MiB      0.0 MiB           3               shuffle(self.player_card[line + 1])


----------Player----------
48    74 61          13 45 
   23 86    38  8    43    
      79 69 67 25 56       
--------------------------
Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     17.3 MiB     17.3 MiB           1       @profile
    34                                             def __str__(self):
    35     17.3 MiB      0.0 MiB          47           [[print(j, end='') for j in i] and print() for i in self.player_card]
    36     17.3 MiB      0.0 MiB           1           return ''


==========================
---------Computer---------
32           2 56    44 74 
      87 28  4 14       38 
      79    77    54  3 19 
--------------------------
Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     17.3 MiB     17.3 MiB           1       @profile
    34                                             def __str__(self):
    35     17.3 MiB      0.0 MiB          47           [[print(j, end='') for j in i] and print() for i in self.player_card]
    36     17.3 MiB      0.0 MiB           1           return ''



Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     17.3 MiB     17.3 MiB           1       @profile
    43                                             def give_me_num(self):
    44     17.3 MiB      0.0 MiB           1           for self.__el in self.roll():
    45     17.3 MiB      0.0 MiB           1               return self.__el


Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   105     17.3 MiB     17.3 MiB           1       @profile
   106                                             def num_from_bag(self):
   107     17.3 MiB      0.0 MiB           1           self._num = self.give_me_num()
   108     17.3 MiB      0.0 MiB           1           if len(rolled) >= 90:
   109                                                     return 0
   110                                         
   111     17.3 MiB      0.0 MiB           1           while self._num in rolled:
   112                                                     self._num = self.give_me_num()
   113     17.3 MiB      0.0 MiB           1           rolled.append(self._num)
   114     17.3 MiB      0.0 MiB           1           return self._num


Выпал бочонок с номером 82
Зачеркнуть? (у/n): y
Вы проиграли!
Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    65     17.3 MiB     17.3 MiB           1       @profile
    66                                             def step(self, current_num):
    67     17.3 MiB      0.0 MiB           1           self._found = False
    68     17.3 MiB      0.0 MiB           1           self.__current_num = current_num
    69     17.3 MiB      0.0 MiB           1           self.user_answer = input('Зачеркнуть? (у/n): ').lower()
    70     17.3 MiB      0.0 MiB           1           if self.__current_num == 0:
    71                                                     print('Бочонков больше не осталось!')
    72                                                     return False
    73     17.3 MiB      0.0 MiB           5           for i in range(1, len(self.player_card)):
    74     17.3 MiB      0.0 MiB          32               for j in self.player_card[i]:
    75     17.3 MiB      0.0 MiB          28                   if str(self.__current_num) in j:
    76                                                             if self.__current_num < 10 and len(j.rstrip().lstrip()) == 1 or \
    77                                                                     (self.__current_num >= 10 and len(j.rstrip()) == 2):
    78                                                                 self._found = True
    79                                                                 if self.user_answer == 'y':
    80                                                                     self.player_card[i][self.player_card[i].index(j)] = '-- '
    81                                                                     if self.__current_num < 10:
    82                                                                         del self._total_in_card[
    83                                                                             self._total_in_card.index(' ' + str(self.__current_num))]
    84                                                                         break
    85                                                                     elif self.__current_num >= 10:
    86                                                                         del self._total_in_card[
    87                                                                             self._total_in_card.index(self.__current_num)]
    88                                                                         break
    89                                         
    90     17.3 MiB      0.0 MiB           1           if (self.user_answer == 'n' and self._found == True) or (self.user_answer == 'y' and self._found == False):
    91     17.3 MiB      0.0 MiB           1               print('Вы проиграли!')
    92     17.3 MiB      0.0 MiB           1               return False


Filename: ***/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   145     17.3 MiB     17.3 MiB           1   @profile
   146                                         def game():
   147     17.3 MiB      0.0 MiB           1       while len(rolled) <= number_of_kegs:
   148     17.3 MiB      0.0 MiB           1           print(a, end='')
   149     17.3 MiB      0.0 MiB           1           print('==========================')
   150     17.3 MiB      0.0 MiB           1           print(b)
   151                                         
   152     17.3 MiB      0.0 MiB           1           keg = a.num_from_bag()
   153     17.3 MiB      0.0 MiB           1           print(f'Выпал бочонок с номером {keg}')
   154                                         
   155     17.3 MiB      0.0 MiB           1           if a.step(keg) == False:
   156     17.3 MiB      0.0 MiB           1               break
   157                                                 elif a.check_win() == True:
   158                                                     print('Игрок победил!')
   159                                                     break
   160                                                 elif b.check_win() == True:
   161                                                     print('Компьютер победил!')
   162                                                     break
   163                                                 b.step(keg)



Process finished with exit code 0


Наблюдения и выводы:
Профилировщик показал, что прироста памяти по ходу выполнения программы нет. Судя по "точечным" замерам 
времени выполнения методов - работают они достаточно быстро. Скорее всего можно увеличить скорость 
выполнения путём замены циклов на рекурсию с мемоизацией (в части перебора значений карточек для проверки) 
в ущерб потребляемой памяти.
'''

# запуски тестов:
number_1()
# number_2()
# number_3()
