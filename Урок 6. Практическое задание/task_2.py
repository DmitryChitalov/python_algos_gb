"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

"""
Вспоминая опыт работы с MySQL первым пунктом вспоминается контроль типов данных
То есть явное указание типов хранимых и передаваемых переменных для экономии ресурсов,
а также контроль неявных преобразований.

# (ложное предположение)
# Там где необходимо обходить массив - проходить по элементам, а не по индексам, т.к. индекс это доп.переменная


При импорте модулей производить импорт только нужных частей, т.к. остальное будет неиспользуемым кодом,
но память занимать всё равно он будет

Файлы читать в бинарном виде, т.к. это не потребут доп.ресурсов для преобразования из бинарного вида в "человеческий"

Отказ от изобретения "велосипедов" в пользу использования готовых (и оптимизированных) модулей

По итогу я ушёл читать хабр (https://habr.com/ru/company/mailru/blog/336156/)
"""
from random import randint
from memory_profiler import profile
import cProfile, pstats

@profile
def index_itr(data: list):
    data_sum = 0
    for idx in range(len(data)):
        data_sum += data[idx]
    print(data_sum)

@profile
def elem_itr(data: list):
    data_sum = 0
    for elem in data:
        data_sum += elem
    print(data_sum)

@profile
def index_itr_3d(data: list):
    data_sum = 0
    for idx in range(len(data)):
        for idx_2 in range(len(data[idx])):
            data_sum += data[idx][idx_2]
    print(data_sum)

@profile
def elem_itr_3d(data: list):
    data_sum = 0
    for elem in data:
        for sub_elem in elem:
            data_sum += sub_elem
    print(data_sum)

my_data = [randint(0, 100) for step in range(50000)]
my_data_3d = []
for i in range(100):
    my_data_3d.append(my_data[:])

profiler = cProfile.Profile()
profiler.enable()

index_itr(my_data)
elem_itr(my_data)
# Вот этот кусочек кода ниже займёт много времени твоей жизни, подумай, а нужно ли тебе оно?
index_itr_3d(my_data_3d)
elem_itr_3d(my_data_3d)

profiler.disable()
stats = pstats.Stats(profiler).sort_stats('tottime')
stats.print_stats()

# Отчёт профилировщиков

# /usr/bin/python3.8 "/home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py"
# 2506992
# Filename: /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     31     56.4 MiB     56.4 MiB           1   @profile
#     32                                         def index_itr(data: list):
#     33     56.4 MiB      0.0 MiB           1       data_sum = 0
#     34     56.4 MiB      0.0 MiB       50001       for idx in range(len(data)):
#     35     56.4 MiB      0.0 MiB       50000           data_sum += data[idx]
#     36     56.4 MiB      0.0 MiB           1       print(data_sum)
#
#
# 2506992
# Filename: /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     38     56.4 MiB     56.4 MiB           1   @profile
#     39                                         def elem_itr(data: list):
#     40     56.4 MiB      0.0 MiB           1       data_sum = 0
#     41     56.4 MiB      0.0 MiB       50001       for elem in data:
#     42     56.4 MiB      0.0 MiB       50000           data_sum += elem
#     43     56.4 MiB      0.0 MiB           1       print(data_sum)
#
#
# 250699200
# Filename: /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     45     56.4 MiB     56.4 MiB           1   @profile
#     46                                         def index_itr_3d(data: list):
#     47     56.4 MiB      0.0 MiB           1       data_sum = 0
#     48     56.4 MiB      0.0 MiB         101       for idx in range(len(data)):
#     49     56.4 MiB      0.0 MiB     5000100           for idx_2 in range(len(data[idx])):
#     50     56.4 MiB      0.0 MiB     5000000               data_sum += data[idx][idx_2]
#     51     56.4 MiB      0.0 MiB           1       print(data_sum)
#
#
# 250699200
# Filename: /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     53     56.4 MiB     56.4 MiB           1   @profile
#     54                                         def elem_itr_3d(data: list):
#     55     56.4 MiB      0.0 MiB           1       data_sum = 0
#     56     56.4 MiB      0.0 MiB         101       for elem in data:
#     57     56.4 MiB      0.0 MiB     5000100           for sub_elem in elem:
#     58     56.4 MiB      0.0 MiB     5000000               data_sum += sub_elem
#     59     56.4 MiB      0.0 MiB           1       print(data_sum)
#
#
#          34406 function calls (33274 primitive calls) in 905.456 seconds
#
#    Ordered by: internal time
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1  450.042  450.042  450.042  450.042 /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py:45(index_itr_3d)
#         1  446.392  446.392  446.392  446.392 /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py:53(elem_itr_3d)
#         1    4.501    4.501    4.501    4.501 /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py:38(elem_itr)
#         1    4.490    4.490    4.490    4.490 /home/mrwindmark/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/task_2.py:31(index_itr)
#     221/5    0.017    0.000    0.019    0.004 /usr/lib/python3.8/sre_parse.py:493(_parse)
#       609    0.001    0.000    0.001    0.000 {built-in method posix.lstat}
#     280/2    0.001    0.000    0.001    0.001 /usr/lib/python3.8/sre_compile.py:71(_compile)
#       609    0.001    0.000    0.001    0.000 /usr/lib/python3.8/posixpath.py:71(join)
#   132/131    0.001    0.000    0.003    0.000 /usr/lib/python3.8/posixpath.py:396(_joinrealpath)
#       263    0.001    0.000    0.001    0.000 /usr/lib/python3.8/posixpath.py:334(normpath)
#       194    0.000    0.000    0.021    0.000 /usr/lib/python3.8/tokenize.py:429(_tokenize)
#    306/29    0.000    0.000    0.001    0.000 /usr/lib/python3.8/sre_parse.py:174(getwidth)
#      1537    0.000    0.000    0.001    0.000 /usr/lib/python3.8/sre_parse.py:164(__getitem__)
#       135    0.000    0.000    0.000    0.000 {built-in method posix.stat}
#      3524    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
# 2549/2239    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       135    0.000    0.000    0.001    0.000 /usr/lib/python3.8/inspect.py:692(getsourcefile)
#       609    0.000    0.000    0.001    0.000 /usr/lib/python3.8/posixpath.py:164(islink)
#       949    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:233(__next)
#         4    0.000    0.000    0.007    0.002 /usr/lib/python3.8/inspect.py:726(getmodule)
#      4349    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      52/2    0.000    0.000    0.019    0.010 /usr/lib/python3.8/sre_parse.py:435(_parse_sub)
#      1004    0.000    0.000    0.000    0.000 /usr/lib/python3.8/posixpath.py:41(_get_sep)
#      1532    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
#       174    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
#       395    0.000    0.000    0.000    0.000 /usr/lib/python3.8/posixpath.py:60(isabs)
#      1272    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
#       263    0.000    0.000    0.001    0.000 /usr/lib/python3.8/posixpath.py:372(abspath)
#       667    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:254(get)
#       170    0.000    0.000    0.021    0.000 /usr/lib/python3.8/re.py:289(_compile)
#        59    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:276(_optimize_charset)
#       270    0.000    0.000    0.000    0.000 {built-in method builtins.any}
#       132    0.000    0.000    0.002    0.000 /usr/lib/python3.8/inspect.py:714(getabsfile)
#         4    0.000    0.000    0.022    0.005 /usr/lib/python3.8/inspect.py:947(getblock)
#      1793    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
#       750    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#       510    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:249(match)
#       131    0.000    0.000    0.004    0.000 /usr/lib/python3.8/posixpath.py:387(realpath)
#       184    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
#       443    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:172(append)
#       478    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:160(__len__)
#       609    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
#       190    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:903(tokeneater)
#        78    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#       522    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:702(<genexpr>)
#       305    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:111(__init__)
#       330    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:63(ismodule)
#       405    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:699(<genexpr>)
#       144    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:654(getfile)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:809(show_results)
#       166    0.000    0.000    0.021    0.000 /usr/lib/python3.8/tokenize.py:98(_compile)
#       263    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
#       214    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:286(tell)
#       166    0.000    0.000    0.000    0.000 /usr/lib/python3.8/types.py:171(__get__)
#       130    0.000    0.000    0.000    0.000 /usr/lib/python3.8/genericpath.py:16(exists)
#       609    0.000    0.000    0.000    0.000 {built-in method _stat.S_ISLNK}
#       190    0.000    0.000    0.000    0.000 <string>:1(__new__)
#        55    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:355(_escape)
#        59    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:249(_compile_charset)
#         4    0.000    0.000  905.426  226.357 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:715(f)
#       170    0.000    0.000    0.021    0.000 /usr/lib/python3.8/re.py:250(compile)
#       263    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#        42    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
#         4    0.000    0.000    0.029    0.007 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:602(add)
#         4    0.000    0.000    0.008    0.002 /usr/lib/python3.8/inspect.py:772(findsource)
#       292    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#         2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
#        51    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:432(_uniq)
#       390    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       190    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x907780}
#       201    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
#        51    0.000    0.000    0.000    0.000 {built-in method fromkeys}
#       132    0.000    0.000    0.000    0.000 /usr/lib/python3.8/posixpath.py:52(normcase)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:659(__init__)
#         4    0.000    0.000  905.456  226.364 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:1140(wrapper)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/tokenize.py:388(open)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:1155(choose_backend)
#       189    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         4    0.000    0.000    0.029    0.007 /usr/lib/python3.8/inspect.py:958(getsourcelines)
#         2    0.000    0.000    0.000    0.000 {built-in method io.open}
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/linecache.py:82(updatecache)
#        62    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:423(_simple)
#       166    0.000    0.000    0.000    0.000 /usr/lib/python3.8/enum.py:664(value)
#        26    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:84(opengroup)
#         2    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
#       152    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/contextlib.py:117(__exit__)
#         4    0.000    0.000    0.029    0.007 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:670(__call__)
#       136    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
#       166    0.000    0.000    0.000    0.000 {method 'span' of 're.Match' objects}
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:738(disable_by_count)
#         6    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#        63    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:168(__setitem__)
#         6    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:413(<listcomp>)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:493(unwrap)
#        57    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:81(groups)
#         6    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:411(_mk_bitmap)
#         8    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:697(_count_ctxmgr)
#         8    0.000    0.000    0.000    0.000 /usr/lib/python3.8/linecache.py:37(getlines)
#         2    0.000    0.000    0.021    0.010 /usr/lib/python3.8/sre_compile.py:759(compile)
#        26    0.000    0.000    0.001    0.000 /usr/lib/python3.8/sre_parse.py:96(closegroup)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:171(_has_code_flag)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/contextlib.py:82(__init__)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/tokenize.py:295(detect_encoding)
#        30    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:652(<genexpr>)
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.next}
#         2    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/linecache.py:53(checkcache)
#         8    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:646(items)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/tokenize.py:325(find_cookie)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:798(enable)
#         1    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
#         2    0.000    0.000    0.019    0.010 /usr/lib/python3.8/sre_parse.py:937(parse)
#        26    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:65(_combine_flags)
#         6    0.000    0.000    0.000    0.000 /usr/lib/python3.8/codecs.py:319(decode)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:536(_compile_info)
#         4    0.000    0.000    0.029    0.007 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:685(add_function)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:805(disable)
#         8    0.000    0.000    0.000    0.000 {built-in method sys.settrace}
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:894(__init__)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/enum.py:833(__and__)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/contextlib.py:238(helper)
#        16    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:260(iscode)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/asyncio/coroutines.py:164(iscoroutinefunction)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/enum.py:283(__call__)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/contextlib.py:108(__enter__)
#        12    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:80(ismethod)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:731(enable_by_count)
#         8    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:72(isclass)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:705(wrap_function)
#        12    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:158(isfunction)
#        12    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:246(isframe)
#         4    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:597(__init__)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/codecs.py:309(__init__)
#        12    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:236(istraceback)
#         2    0.000    0.000    0.002    0.001 /usr/lib/python3.8/sre_compile.py:598(_code)
#        12    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:295(_class_escape)
#        16    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/dist-packages/memory_profiler.py:1167(<genexpr>)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:510(_is_wrapper)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/inspect.py:189(iscoroutinefunction)
#         9    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
#         4    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/tokenize.py:612(generate_tokens)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:224(__init__)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/enum.py:562(__new__)
#         1    0.000    0.000    0.000    0.000 {built-in method posix.readlink}
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:921(fix_flags)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/functools.py:429(_unwrap_partial)
#         6    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
#         4    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/tokenize.py:319(read_or_stop)
#         2    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_parse.py:76(__init__)
#         4    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:595(isstring)
#         1    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:492(_get_charset_prefix)
#         1    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:461(_get_literal_prefix)
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/codecs.py:260(__init__)
#         4    0.000    0.000    0.000    0.000 {built-in method sys.gettrace}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.id}
#         4    0.000    0.000    0.000    0.000 {built-in method sys.getrecursionlimit}
#         8    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#         2    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
#         3    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#         2    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
#         2    0.000    0.000    0.000    0.000 /usr/lib/python3.8/sre_compile.py:453(_get_iscased)
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
#         1    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}