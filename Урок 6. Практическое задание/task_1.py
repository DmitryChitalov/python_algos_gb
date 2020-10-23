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

import hashlib, uuid, time, requests
from memory_profiler import profile
from timeit import timeit
from pympler import asizeof


"""
О системе:
Python 3.8
Win10 x641
"""


###################################
"""
Профилирование памяти
Поиск простых чисел

На примере задачи 5 с урока 4 попробую профилирование с использованием Memory_profiler.
Так же для наглядности буду использовать замер времени с использованием timeit
"""


@profile
def simple(i):
    """Без использования «Решета Эратосфена»
    Сложность: O(4n**2 + 5n + 2)
    """
    count = 1                                       # O(1)
    n = 2                                           # O(1)
    while count <= i:                               # O(n * (4n + 5)) = O(4n**2 + 5n)
        t = 1                                       # O(1)
        is_simple = True                            # O(1)
        while t <= n:                               # O(4n)
            if n % t == 0 and t != 1 and t != n:    # O(3)
                is_simple = False                   # O(1)
                break
            t += 1                                  # O(1)
        if is_simple:                               # O(2)
            if count == i:                          # O(1)
                break
            count += 1                              # O(1)
        n += 1                                      # O(1)
    return n


@profile
def simple_eratosfen(i):
    """Функция поиска i-го элемента в ряде простых чисел.
    Используется алгоритм Решето Эратосфена.

    Сложность: O(n**2 + 3n + 5)

    :param i: порядковый номер искомого элемента в ряде
    :return: Возвращает i-й элемент ряда простых чисел
    """
    simples = [2]                       # O(1)
    n = simples[len(simples) - 1] + 1   # O(3)
    while len(simples) < i:             # O(1 + n * (n + 3)) = O(n**2 + 3n + 1)
        is_simple = True                # O(1)
        for s in simples:               # O(n)
            if n % s == 0:              # O(1)
                is_simple = False       # O(1)
                break
        if is_simple:                   # O(1)
            simples.append(n)           # O(1)
        n += 1                          # O(1)
    return simples[len(simples) - 1]


print("\nПрофилирование функций по поиску i-го простого числа")
i = 200
print(simple(i))
print(simple_eratosfen(i))
setup = "from __main__ import simple, i"
print(f"Время выполнения simple(): {timeit('simple(i)', setup, number=1)}")
setup = "from __main__ import simple_eratosfen, i"
print(f"Время выполнения simple_eratosfen(): {timeit('simple_eratosfen(i)', setup, number=1)}")

"""
Вывод по профилированию функций поиска i-го простого числа:
Memory_profiler не выявил потребление памяти, т.к.:
  - в первом случае - функция simple() - списков и им подобных вообще нет, только элементарные переменные;
  - во втором случае - simple_eratosfen() - список даже из 500 элементов занимает не много памяти.
Зато Memory_profiler показал количество итераций при поиске простых чисел:
  - 115669 итераций - в первом случае;
  - 22098 итераций - во втором случае.
Чем и обусловлена лучшая производительность второго варианта с функцией simple_eratosfen().
Это же доказывает замер времени с помощью timeit:
  - 14.424 - simple(200);
  - 1.934  - simple_eratosfen(200)
От сюда вывод:
Профилироание эффективности использования памяти целесообразно использовать на функциях,
где ожидаются заведомо большие (более 1000 элементов) списки и т.п.
"""


#####################################
"""
Профилирование памяти
Кэширование веб-страниц

На примере задания 4 урока 3 буду профилировать память программы кэширования страниц.
Программа выполнена в ООП.
"""

sites = ['yandex.ru', 'geekbrains.ru', 'json.parser.online.fr', 'mail.ru', 'google.ru']


class ContentCaching:

    def __init__(self, cache_life=30):
        self.__cache = dict()
        self.__cache_life = int(cache_life)
        self.__salt = uuid.uuid4().hex

    def __check_cache(self, url_hash):
        """Метод проверки наличия данных в кэше и их годность

        :param url_hash: захешированный URL
        :return: Возвращает контент если есть, либо None
        """
        cache = self.__cache.get(url_hash)
        if cache is not None and cache['timeout'] > time.time():
            return cache['content']
        else:
            return None

    def __set_cache(self, url, content):
        """Метод записи контента страницы в кэш

        :param url: URL адрес страницы
        :param content: Контент страницы (HTML-код)
        """
        url_hash = self.__url_hash(url)
        self.__cache[url_hash] = {
            'timeout': int(time.time()) + self.__cache_life,
            'url': url,
            'content': content
        }

    def cache_clear(self):
        self.__cache = dict()

    def status_cache(self):
        """Метод вывода статуса кэша

        :return: Выводит в терминал состояние кэша
        """
        print(f"\n{'- ' * 30}\nСтатус кэша:\n * Всего в кэше: {len(self.__cache)}")
        for i, cache in enumerate(self.__cache):
            row = f"\t{i}: "
            row += f"hash: {cache}, "
            row += f"time left: {int(self.__cache[cache]['timeout'] - time.time()) if self.__cache[cache]['timeout'] > time.time() else 'протухло'}, "
            row += f"url: {self.__cache[cache]['url']}, "
            row += f"длина контента: {len(self.__cache[cache]['content'])}"
            print(row)
        print('- ' * 30, end="\n\n")

    def __url_hash(self, url):
        """Метод хеширует URL-адрес

        :param url: URL адрес страницы
        :return: Возвращает захешированный URL страницы
        """
        return hashlib.md5(self.__salt.encode() + url.encode()).hexdigest()

    def get_content(self, url):
        """Метод получения контента страницы

        :param url: URL адрес страницы
        :return: Возвращает контент страницы (HTML-код)
        """
        if url.find('http://') != 0 and url.find('https://') != 0:
            url = 'http://' + url
        url_hash = self.__url_hash(url)
        content = self.__check_cache(url_hash)
        if content is not None:
            return content
        else:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    self.__set_cache(url, r.text)
                return r.text
            except:
                return ''


#################################
@profile
def site_caching():
    cc = ContentCaching()
    size_obj = asizeof.asizeof(cc)
    print(f"Размер объекта ContentCaching(): {size_obj}")
    for s in sites:
        site_content = cc.get_content(s)
        print(f"Длина тела ответа: {len(site_content)}")
    print(f"Размер объекта ContentCaching(): {asizeof.asizeof(cc)}")
    print(f"Разница размера объекта с данными и без: {asizeof.asizeof(cc) - size_obj}")
    cc.status_cache()
    cc.cache_clear()
    cc.status_cache()


# Запуск теста
print("\nПрофилирование кэширования веб-страниц")
site_caching()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   208     19.5 MiB     19.5 MiB           1   @profile
   209                                         def site_caching():
   210     19.5 MiB      0.0 MiB           1       cc = ContentCaching()
   211     23.5 MiB     -0.6 MiB           6       for s in sites:
   212     23.5 MiB      3.4 MiB           5           site_content = cc.get_content(s)
   213     23.5 MiB     -0.6 MiB           5           print(f"Длина тела ответа: {len(site_content)}")
   214     23.0 MiB     -0.5 MiB           1       cc.status_cache()
   215     21.9 MiB     -1.1 MiB           1       cc.cache_clear()
   216     21.9 MiB      0.0 MiB           1       cc.status_cache()

Получение контента веб-страниц и сохранение их в кэше занимает 3.4 MiB.

Замеры размера объекта:
 - 448 - пустой объект ContentCaching()
 - 1090848 - объект с кэшем

Далее пробую сделать тот же класс, но уже с использванием слотов.
"""


class ContentCachingSlots:

    __slots__ = ['__cache', '__cache_life', '__salt']

    def __init__(self, cache_life=30):
        self.__cache = dict()
        self.__cache_life = int(cache_life)
        self.__salt = uuid.uuid4().hex

    def __check_cache(self, url_hash):
        """Метод проверки наличия данных в кэше и их годность

        :param url_hash: захешированный URL
        :return: Возвращает контент если есть, либо None
        """
        cache = self.__cache.get(url_hash)
        if cache is not None and cache['timeout'] > time.time():
            return cache['content']
        else:
            return None

    def __set_cache(self, url, content):
        """Метод записи контента страницы в кэш

        :param url: URL адрес страницы
        :param content: Контент страницы (HTML-код)
        """
        url_hash = self.__url_hash(url)
        self.__cache[url_hash] = {
            'timeout': int(time.time()) + self.__cache_life,
            'url': url,
            'content': content
        }

    def cache_clear(self):
        self.__cache = dict()

    def status_cache(self):
        """Метод вывода статуса кэша

        :return: Выводит в терминал состояние кэша
        """
        print(f"\n{'- ' * 30}\nСтатус кэша:\n * Всего в кэше: {len(self.__cache)}")
        for i, cache in enumerate(self.__cache):
            row = f"\t{i}: "
            row += f"hash: {cache}, "
            row += f"time left: {int(self.__cache[cache]['timeout'] - time.time()) if self.__cache[cache]['timeout'] > time.time() else 'протухло'}, "
            row += f"url: {self.__cache[cache]['url']}, "
            row += f"длина контента: {len(self.__cache[cache]['content'])}"
            print(row)
        print('- ' * 30, end="\n\n")

    def __url_hash(self, url):
        """Метод хеширует URL-адрес

        :param url: URL адрес страницы
        :return: Возвращает захешированный URL страницы
        """
        return hashlib.md5(self.__salt.encode() + url.encode()).hexdigest()

    def get_content(self, url):
        """Метод получения контента страницы

        :param url: URL адрес страницы
        :return: Возвращает контент страницы (HTML-код)
        """
        if url.find('http://') != 0 and url.find('https://') != 0:
            url = 'http://' + url
        url_hash = self.__url_hash(url)
        content = self.__check_cache(url_hash)
        if content is not None:
            return content
        else:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    self.__set_cache(url, r.text)
                return r.text
            except:
                return ''


#################################
@profile
def site_caching_slots():
    cc = ContentCachingSlots()
    size_obj = asizeof.asizeof(cc)
    print(f"Размер объекта ContentCachingSlots(): {size_obj}")
    for s in sites:
        site_content = cc.get_content(s)
        print(f"Длина тела ответа: {len(site_content)}")
    print(f"Размер объекта ContentCachingSlots(): {asizeof.asizeof(cc)}")
    print(f"Разница размера объекта с данными и без: {asizeof.asizeof(cc) - size_obj}")
    cc.status_cache()
    cc.cache_clear()
    cc.status_cache()


# Запуск теста
print("\nПрофилирование кэширования веб-страниц с использованием слотов")
site_caching_slots()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   311     21.9 MiB     21.9 MiB           1   @profile
   312                                         def site_caching_slots():
   313     21.9 MiB      0.0 MiB           1       cc = ContentCachingSlots()
   314     23.6 MiB     -0.7 MiB           6       for s in sites:
   315     23.6 MiB      0.9 MiB           5           site_content = cc.get_content(s)
   316     23.6 MiB     -0.7 MiB           5           print(f"Длина тела ответа: {len(site_content)}")
   317     23.1 MiB     -0.5 MiB           1       cc.status_cache()
   318     22.0 MiB     -1.1 MiB           1       cc.cache_clear()
   319     22.0 MiB      0.0 MiB           1       cc.status_cache()

Теперь те же запросы и сохранение в кэше занимает значительно меньше места - 0.9 MiB - в стравнении с первым вариантом.

Замеры размера объекта:
 - 240 - пустой объект ContentCachingSlots()
 - 1090672 - объект с кэшем
 
От сюда можно сделать вывод что для классов, которые предполагают хранение множество различных свойств
и содержат много методов, то лучше использовать слоты.
Предполагаю что в моем примере меньше места занимает скорее именно сам экземпляр класса (объект),
а не объем кэша, т.к. кэш и в слотах остался словарем.
Для оптимизации использования памяти надо было бы хранить кэш, к примеру, в кортежах, или даже в множествах.
"""
