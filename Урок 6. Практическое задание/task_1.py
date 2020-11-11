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
from pympler import asizeof
import collections
from numpy import mean, array, append, arange
from itertools import chain

### begin 1/1
'''
company = collections.namedtuple('profit', 'company one two three four')

#@profile
def go_():
    nCompany = input('Введите кол-во предприятий: ')
    all_company = []
    for i in range(int(nCompany)):
        temp_str = input('Через пробел введите: название и квартальные прибыли для каждой: ')
        return_company = company(company = temp_str.split(' ')[0],
                                one=temp_str.split(' ')[1],
                                two=temp_str.split(' ')[2],
                                three=temp_str.split(' ')[3],
                                four=temp_str.split(' ')[4])
        all_company.append(return_company)
    return all_company

#@profile
def out_():
    list_company = go_()
    profit = []
    for i in list_company:
        for ii in i[1:]:
            profit.append(int(ii))
    return_str = f'средняя годовая прибыль всех компаний = {mean(profit)}; \
    \n меньше годовой: {min(list_company)[0]}; \
    \n больше годовой: {max(list_company)[0]};'
    return return_str

print(asizeof.asizeof(out_()))
# у меня получилось 264, 
# я всё это помещу в комментарии, чтобы не мешало

# profile вообще ничего не показывает. Его использовать не вижу смысла.
### end 1/1
'''

### begin 1/2

company = collections.namedtuple('profit', 'company one two three four')
#@profile
def out_():
    #list_company = go_()

    list_company = array([company(company=q[0],
                             one=q[1],
                             two=q[2],
                             three=q[3],
                             four=q[4]) for q in
                     [array([iii for iii in
                                   input('Через пробел введите: название и квартальные прибыли для каждой: ').split(
                                       ' ')])
                      for ii
                      in array([i for i in arange(int(input('Введите кол-во предприятий: ')))])]])

    print(list_company)
    # всё, дальше я сдаюсь.
    # Решил, что получится сделать всё в одну строку,
    # бьюсь уже шестой час, перестал понимать, что тут происходит
    print(f'средняя прибыль всех предприятий: {mean(array([int(n) for n in list(chain.from_iterable([i[1:] for i in [ii for ii in list_company]]))]))}')
    # max и min вообще отказываются выполняться для list_company. Не понимаю, почему

print(asizeof.asizeof(out_()))
# Возвращается число "16", что разительно отличается от "264".
# В общем, было увлекательно, но не продуктивно.
# Чувство удовлетворения присутствует, но на оставшееся задания уже нет времени.

### end 1/2