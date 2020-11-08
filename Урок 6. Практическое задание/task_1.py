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
from pympler import asizeof
import struct
from timeit import default_timer, timeit


# 1. Задача из основ
# вариант решения до профилирования

class Worker:
    def __init__(self, name, surname, pos, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = pos
        if not (isinstance(wage, int) or isinstance(bonus, float) or
                isinstance(wage, int) or isinstance(bonus, float)):
            print('Оклад и премия должны быть числами!')
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return print(f'{self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        return print('Доход с учетом премии:', self._income['wage'] + self._income['bonus'])


# вариант решения после профилирования и анализа

class StructWorker:
    """используем slots и struct"""

    __slots__ = ('_data',)  # выделяем под будущий экземпляр класса один object (StructWorker._data)
    Data = struct.Struct('20s30s30sll')  # под один символ латиницы резервируем два байта
    """"
    Struct object, упаковываем числа (зарплата, премия) в long integer (используем class struct.Struct),
    имя, фамилию и должность упаковываем в char c указанием длины строки.
    """

    def __init__(self, name, surname, pos, wage, bonus):
        """Упаковываем все данные в один объект"""
        self._data = StructWorker.Data.pack(name.encode('utf-8'), surname.encode('utf-8'), pos.encode('utf-8'),
                                            wage, bonus)

    @property
    def name(self):
        return StructWorker.Data.unpack(self._data)[0]

    @property
    def surname(self):
        return StructWorker.Data.unpack(self._data)[1]

    @property
    def pos(self):
        return StructWorker.Data.unpack(self._data)[2]

    @property
    def bonus(self):
        return StructWorker.Data.unpack(self._data)[3] + StructWorker.Data.unpack(self._data)[4]


class StructPosition(StructWorker):
    def get_full_name(self):
        return print(f'{self.name.decode("utf-8")} {self.surname.decode("utf-8")}, {self.pos.decode("utf-8")}')

    def get_total_income(self):
        return print(f'Доход с учетом премии: {self.bonus}')


def time_decorator(some_func):
    """
    Вычисляет время выполения декорируемой функции. Сравним скорость работы непрофилированного и профилированного
    вариантов
    """

    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} составило {default_timer() - start}.')
        return result

    return wrapper


if __name__ == '__main__':
    @time_decorator
    def app1():
        """Запускаем первый вариант без профилирования"""

        worker1 = Position(name='Иван', surname='Иванов', pos='инженер', wage=50000, bonus=3000)
        worker1.get_full_name()
        worker1.get_total_income()
        worker2 = Position(name='Петр', surname='Петров', pos='менеджер', wage=65000, bonus=4000)
        worker2.get_full_name()
        worker2.get_total_income()
        print(f'Затраты памяти при создании ста экземпляров: {asizeof.asizeof(worker1) + asizeof.asizeof(worker2)}')

    @time_decorator
    def app2():
        """Запускаем второй вариант без профилирования"""
        worker3 = StructPosition(name='Иван', surname='Иванов', pos='инженер', wage=50000, bonus=3000)
        worker3.get_full_name()
        worker3.get_total_income()
        worker4 = StructPosition(name='Петр', surname='Петров', pos='менеджер', wage=65000, bonus=4000)
        worker4.get_full_name()
        worker4.get_total_income()
        print(f'Затраты памяти при создании двух экземпляров: {asizeof.asizeof(worker3) + asizeof.asizeof(worker4)}')


    app1()
    print('-' * 160)
    app2()
"""
Python 3.8, 64 разряда.
Профилированный вариант при создании экземпляров классов дает экономию памяти примерно в три раза за счет использования
slots и модуля struct, который упаковывает данные экземпляраав байты и распаковывает их только при необходимости, не 
выделяя постоянно в памяти место для их хранения по отдельности. Также отказываемся от словаря, экономя место за счет 
отсутствия необходимости хранения хеш. Скоости работы сопоставимы. При замерах с помощью самодельного декоратора 
профилированный вариант работает даже быстрее, чем не профилированный, так как не тратим время на заполнение словаря,
доступ осуществляем по индексам.
"""