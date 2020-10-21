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

'''
# Python 3.8 OC Windows 64-bit

Пример 1 В данном примере нет проблем с памятью, т.к. мы используем yield и ленивые вычисления и profile ничего не отображает,
но задача узнать сколько же памяти потребовалось. Поэтому сделал подсчет Mib как на уроке.
Результат 0.00390625 Mib, т.к. использовал ленивые вычисления, то при любом значении n количество
затрачиваемых Mib не меняется. Так же поработал с ссылками и guppy
'''

from sys import getrefcount
import memory_profiler
from memory_profiler import profile


@profile
def fact(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
        print(f'Ссылки: {getrefcount(temp)}')
        # т.к. profile ничего не выдает рещил сделать подсчет ссылок и увидел,
        # что ссылке 2, а всего за время операций 653 ссылки
        yield temp


n = 1000  # "Укажите факториал какого числа Вы хотели бы узнать?
for el in fact(n):
    break

if __name__ == "__main__":
    fact(n)
    m1 = memory_profiler.memory_usage()
    m2 = memory_profiler.memory_usage()
    mem_diff = m2[0] - m1[0]

    print(f'\nВыполнение заняло {mem_diff} Mib')

print('*' * 150)

""" 
Пример 2. Поработал с asizeof, без фукции array занимаемая память 12 128 байт 
с функцией array 1 312 байт в 9 раз быстрее. Так же посмотрел как работает hpy
"""

from pympler import asizeof
from numpy import array
from random import randint
from guppy import hpy

number_list = [randint(20, 100000) for i in range(300)]
# print(number_list)
print(f'{asizeof.asizeof(number_list)} байт')

number_list1 = array([randint(20, 100000) for i in range(300)])
print(f'{asizeof.asizeof(number_list1)} байт')

number_list1 = hpy()
print(number_list1.heap())


# my_list = [el for el in number_list if number_list.count(el) == 1]
# print(my_list)

print('*' * 150)


"""
Пример 3. Написаная мною с помощью ООП работа на входе потребляеи 18.8 Mib, а на выходе 0 Mib.
P.s. Упростил код, чтобы при проверке был более читабельный, результаты поменялся на входе 30.2  Mib
на выходе 30.1 MiB при этом на выходе 0.1 Mib у первых данных bmw. Подскажите почему так?
Добавил между первым и третьим примером, второй и количество Mib в 3-ем примере увеличилось, стало 35,7 Mib
"""

class Car:

    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed != 0:
            pass
            # print(f'{self.color} {self.name} проехала со скоростью {self.speed}')

    def stop(self):
        if self.speed == 0:
            pass
            # print(f'{self.color} {self.name} остановилась')

    def turn(self, direction):
        pass
        # print(f'{self.color} {self.name} повернула {direction}')

    def police(self):
        if self.is_police:
            pass
            # print('Полицейская машина')
        else:
            pass
            # print('Не полицейская машина')

    def show_speed(self):
        pass
        # print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            pass
            # print(f'{self.color} {self.name} привысил скорость на: {self.speed - 40}')
        else:
            pass
            # print('Скорость нормальная')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            pass
            # print(f'{self.color} {self.name} привысили скорость на: {self.speed - 40}')
        else:
            pass
            # print('Скорость нормальная')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


@profile
def func():
    bmw = Car(60, 'red', 'bmw')
    bmw.go()
    bmw.stop()
    bmw.turn('прямо')
    bmw.turn('назад')
    bmw.turn('влево')
    bmw.turn('вправо')
    bmw.show_speed()
    opel = TownCar(75, 'Зеленый', 'Opel')
    opel.go()
    opel.stop()
    opel.show_speed()
    truck = WorkCar(50, 'Жёлтый', 'Зил')
    truck.go()
    truck.show_speed()
    mercedes = SportCar(150, 'blue', 'Mercedes')
    mercedes.go()
    mercedes.turn('влево')
    oka = PoliceCar(90, 'yellow', 'Oka')
    oka.go()
    oka.police()


func()
