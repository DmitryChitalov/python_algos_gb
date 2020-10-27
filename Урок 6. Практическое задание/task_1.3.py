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
import time
import memory_profiler


# задача на сложение и умножение шестнадцатиричных чисел
class Hexadecimal:
    __slots__ = ['translate', 'lst']
    translate = {'0': 0,
                 '1': 1,
                 '2': 2,
                 '3': 3,
                 '4': 4,
                 '5': 5,
                 '6': 6,
                 '7': 7,
                 '8': 8,
                 '9': 9,
                 'A': 10,
                 'B': 11,
                 'C': 12,
                 'D': 13,
                 'E': 14,
                 'F': 15,
                 0: '0',
                 1: '1',
                 2: '2',
                 3: '3',
                 4: '4',
                 5: '5',
                 6: '6',
                 7: '7',
                 8: '8',
                 9: '9',
                 10: 'A',
                 11: 'B',
                 12: 'C',
                 13: 'D',
                 14: 'E',
                 15: 'F'}

    def __init__(self, lst):
        self.lst = lst[:]

    def __str__(self):
        return str(self.lst)

    def __add__(self, other):
        res = []
        p = 0
        for i in range(max(len(self.lst), len(other.lst))):
            el1 = self.lst[-i - 1] if i < len(self.lst) else '0'
            el2 = other.lst[-i - 1] if i < len(other.lst) else '0'
            sum = self.translate[el1] + self.translate[el2] + p
            p = sum // 16
            res.append(self.translate[sum % 16])
        return Hexadecimal(res[::-1])

    def __mul__(self, other):
        res = Hexadecimal([])
        count = 0
        for el2 in other.lst[::-1]:
            buf = []
            p = 0
            for el1 in self.lst[::-1]:
                m = self.translate[el1] * self.translate[el2] + p
                p = m // 16
                buf.append(self.translate[m % 16])
            if p:
                buf.append(self.translate[p])
            buf = buf[::-1]
            for i in range(count):
                buf.append(self.translate[0])
            count += 1
            res = res + Hexadecimal(buf)

        return res


if __name__ == '__main__':
    x = list(input('Введите первое шестнадцатиричное число: ').upper())
    a = Hexadecimal(x)
    y = list(input('Введите второе шестнадцатиричное число: ').upper())
    b = Hexadecimal(y)

    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()
    c = a + b
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()
    с2 = a * b
    t3 = time.process_time()
    m3 = memory_profiler.memory_usage()

    time_diff1 = t2 - t1
    time_diff2 = t3 - t2
    mem_dif1 = m2[0] - m1[0]
    mem_dif2 = m3[0] - m2[0]

print(
    f'Время на первое выражение:{time_diff1}, память  {time_diff2}, время на второе выражение {time_diff2}, память {mem_dif2}')
# решение не затратно ни по времени, ни по памяти
# Вопрос - почему памяти на умножение ушло меньше, чем на сложение, хотя должно быть наоборот?
