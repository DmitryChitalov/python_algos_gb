"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса
Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from pympler import asizeof
import uuid
import hashlib
import urllib.request
import random

class WebCacher:
    """
    В классе WebCacher атрибуты помещены в кортеж, что позволило почти в
    2 раза уменьшить потребление памяти для хранения созданного
    экземляра класса.
    """
    __slots__ = ('_cache', '_salt')

    @profile()
    def __init__(self):
        self._cache = {}
        self._salt = uuid.uuid4().bytes

    @profile()
    def _hash(self, url: str):
        return hashlib.sha256(url.encode() + self._salt).hexdigest()

    @profile()
    def _content(self, url: str):
        with urllib.request.urlopen(url) as c:
            if c.getcode() == 200:
                return c.read()
            else:
                print(f"Can't get content on link {url}.")

    @profile()
    def cached(self, url: str):
        return bool(self._cache.get(self._hash(url)))

    @profile()
    def add_to_cash(self, url: str):
        if self._content(url):
            self._cache[self._hash(url)] = self._content(url)
        if not self.cached(url):
            print('Cashing was failed.')

if __name__ == '__main__':
    url_list = ['https://geekbrains.ru', 'https://www.google.com/']
    casher = WebCacher()
    print(f'Размер экземпляра класса WebCasher: {asizeof.asizeof(casher)}')
    casher.add_to_cash(url_list[0])
    for url in url_list:
        print(f'{url} is in cache.') if casher.cached(url) else \
            print(f'{url} is not in cache.')

@profile()
def func_1(nums):
    """
    Преобразование результирующего списка в кортеж позволяет
    незначительно экономить память при использовании функции func_1.
    Впрочем разница становится заметна при больших порядках длины
    обрабатываемого массива.
    """
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    print(f'Размер списка: {asizeof.asizeof(new_arr)}')
    new_arr = tuple(new_arr)
    print(f'Размер кортежа: {asizeof.asizeof(new_arr)}')
    return new_arr

func_1([i for i in range(10000)])

"""
Для профилирования памяти я воспользовался инструментами из модулей
pympler и memory_profiler. Рассмотрев свои алгоритмы, я пришёл к выводу,
что в целом пишу оптимальный с точки зрения использования памяти код.
Однако стоит обратить особое внимание на использование генераторов, их
я применяю несколько реже, чем иные способы оптимизации.
"""