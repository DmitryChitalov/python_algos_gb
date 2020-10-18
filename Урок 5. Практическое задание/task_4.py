"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from collections import defaultdict
from timeit import timeit

res = defaultdict(list)
# Операции с упорядоченным словарём.
odict = OrderedDict({i: i for i in range(1000)})
dct = {i: i for i in range(1001,1011)}

stmts = ('get', 'move_to_end', 'setdefault')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"odict.{stmt}(20)", setup='from __main__ import odict',
               number=10000))
res['update'].append(timeit(f"odict.update(dct)",
                    setup='from __main__ import odict, dct', number=10000))
res['fromkeys'].append(timeit(f"odict.fromkeys((-2, -2))",
                              setup='from __main__ import odict',
                              number=10000))
stmts = ('keys', 'values', 'items', 'copy', 'popitem', 'clear')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"odict.{stmt}",
               setup='from __main__ import odict', number=10000))



# Операции со словарём.
dct = {i: i for i in range(1000)}
dct_2 = {i: i for i in range(1001,1011)}

stmts = ('get', 'setdefault')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"dct.{stmt}(20)", setup='from __main__ import dct',
               number=10000))
res['update'].append(timeit(f"dct.update(dct_2)",
                    setup='from __main__ import dct, dct_2', number=10000))
res['fromkeys'].append(timeit(f"dct.fromkeys((-2, -2))",
                              setup='from __main__ import dct',
                              number=10000))
stmts = ('keys', 'values', 'items', 'copy', 'popitem', 'clear')
for stmt in stmts:
    res[f'{stmt}'].append(
        timeit(f"dct.{stmt}",
               setup='from __main__ import dct', number=10000))

# Выводим результаты.
for k,v in res.items():
    print(f'Операция {k}:')
    if len(v) == 2:
        print(f'у/словарь: {v[0]:<20f}словарь: {v[1]:<20f}')
    else:
        print(f'у/словарь: {v[0]:<20f}словарь: нет аналогичной операции')

"""
Выводы:
- современная реализация словарей в python по скорости всех операций
  превосходит упорядоченные словари.
Таким образом в использовании упорядоченных словарей при запуске
программ на интерпретаторе версии 3.6+ нет смысла. При использовании же
устаревших версий python свойство у/словарей сохранять порядок элементов
остаётся крайне полезным.
"""