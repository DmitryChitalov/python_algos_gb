from memory_profiler import profile
import asyncio


@profile
# цикл
def c_ascii_print():
    for i in range(32, 128):
        print("%4d-%s" % (i, chr(i)), end='')
        if i % 10 == 0:
           print()
    print()


@profile
# рекурсия
async def ascii_print(i=32):
    if i == 128:
        return
    else:
        print("%4d-%s" % (i, chr(i)), end='')
        if i % 10 == 0:
            print()
        return ascii_print(i + 1)


print('цикл')
c_ascii_print()

print('рекурсия')
loop = asyncio.get_event_loop()
loop.run_until_complete(ascii_print())

#ascii_print()

"""
Выполнено прифилирование использования памяти для задачи печати ascii символов.

Первая реализация через цикл использует 19,5 MiB. Более эффективна по использованию памяти.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     19.5 MiB     19.5 MiB           1   @profile
    25                                         # цикл
    26                                         def c_ascii_print():
    27     19.5 MiB      0.0 MiB          97       for i in range(32, 128):
    28     19.5 MiB      0.0 MiB          96           print("%4d-%s" % (i, chr(i)), end='')
    29     19.5 MiB      0.0 MiB          96           if i % 10 == 0:
    30     19.5 MiB      0.0 MiB           9               print()
    31     19.5 MiB      0.0 MiB           1       print()
    
Вторая реализация через рекурсию использует 20,4 MiB
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     20.4 MiB     20.4 MiB           1   @profile
    35                                         # рекурсия
    36                                         def ascii_print(i=32):
    37     20.4 MiB      0.0 MiB           1       if i == 128:
    38     20.4 MiB      0.0 MiB           1           return
    39                                             else:
    40                                                 print("%4d-%s" % (i, chr(i)), end='')
    41                                                 if i % 10 == 0:
    42                                                     print()
    43                                                 return ascii_print(i + 1)

    
"""