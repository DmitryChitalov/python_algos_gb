
from memory_profiler import profile, memory_usage
import time
import csv
import cProfile


def time_memory_decorator(tmd):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        m1 = memory_usage()
        ans = tmd(*args, **kwargs)
        print(f'Время выполнения: {time.time() - time_start}')
        m2 = memory_usage()
        print(f'Расход памяти: {m2[0] - m1[0]}')
        return ans

    return wrapper


def profile2(func):
    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + '.prof'
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result
    return wrapper


@time_memory_decorator
def prof():
    reverse_number = []

    def reverse(number):
        if len(number) == 1:
            reverse_number.append(number[0])
            stroka = "".join(reverse_number)
            # print("Перевернутое число:")
            return f'Перевернутое число:{stroka}'

        reverse_number.append(number[-1])
        return reverse(number[0:len(number) - 1])

    print(reverse("12300"))

def start():
    def start_pr1():
        prof()
        print()

    @profile
    def start_pr2():
        prof()
        print()

    @profile2
    def start_pr3():
        prof()
        print()

    start_pr1()
    start_pr2()
    start_pr3()


start()


# "C:\Program Files\Python39\python.exe" "C:/Users/YAROSLAR/OneDrive - AMDOCS/Backup Folders/Desktop/Рабочие файлы/lesson 6/6.1.3.py"
# Перевернутое число:11111110001234567890987654321
# Время выполнения: 0.10020661354064941
# Расход памяти: 0.01953125
#
# Перевернутое число:11111110001234567890987654321
# Время выполнения: 0.10042881965637207
# Расход памяти: 0.015625
#
# Filename: C:\Users\YAROSLAR\OneDrive - AMDOCS\Backup Folders\Desktop\Рабочие файлы\lesson 6\6.1.3.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     52     16.5 MiB     16.5 MiB       @profile
#     53                                 def start_pr2():
#     54     16.6 MiB      0.0 MiB           prof()
#     55     16.6 MiB      0.0 MiB           print()
#
#
# Перевернутое число:11111110001234567890987654321
# Время выполнения: 0.10062146186828613
# Расход памяти: 0.0078125
#
#
# Process finished with exit code 0



# ДЛЯ ДЛИННОГО ЧИСЛА
# -------------------
# ДЛЯ КОРОТКОГО ЧИСЛА


# "C:\Program Files\Python39\python.exe" "C:/Users/YAROSLAR/OneDrive - AMDOCS/Backup Folders/Desktop/Рабочие файлы/lesson 6/6.1.3.py"
# Перевернутое число:00321
# Время выполнения: 0.10016679763793945
# Расход памяти: 0.0078125
#
# Перевернутое число:00321
# Время выполнения: 0.10087037086486816
# Расход памяти: 0.0
#
# Filename: C:\Users\YAROSLAR\OneDrive - AMDOCS\Backup Folders\Desktop\Рабочие файлы\lesson 6\6.1.3.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     52     16.6 MiB     16.6 MiB       @profile
#     53                                 def start_pr2():
#     54     16.6 MiB      0.0 MiB           prof()
#     55     16.6 MiB      0.0 MiB           print()
#
#
# Перевернутое число:00321
# Время выполнения: 0.1107168197631836
# Расход памяти: 0.0078125
#
#
# Process finished with exit code 0



# ДЛЯ ДЛИННОГО ЧИСЛА
#без
# Время выполнения: 0.10020661354064941
# Расход памяти: 0.01953125

# mem_pr
# Время выполнения: 0.10042881965637207
# Расход памяти: 0.015625

# cPr
# Время выполнения: 0.10062146186828613
# Расход памяти: 0.0078125

# -------------------
# ДЛЯ КОРОТКОГО ЧИСЛА

#без
# Время выполнения: 0.10016679763793945
# Расход памяти: 0.0078125

# mem_pr
# Время выполнения: 0.10087037086486816
# Расход памяти: 0.0

# cPr
# Время выполнения: 0.1107168197631836
# Расход памяти: 0.0078125



# Время выполнения в пределах погрешности
# А вот затрачиваемая память различается существенно

# для длинных чисел mem_pr умеренную эффективность в 20%, в то время как cProfiler показал экономию примерно в 2.7 раза
#
# а вот при коротких значениях все преимущество cProfiler уходит - результат такой же, как и при работе без профайлера вовсе
# Результаты мем.профайлера узнать не удалось, ибо измеряемое значение ниже порога восприятия встроенного измерителя
#
# Таким образом, после 3 серий тестов наиболее оптимальным показал себя cProfiler, существенно улучшив быстродействие
# и уменьшив затраты памяти в предложенных скриптах. Однако его использование целесообразно лишь при больших и сложных скриптах.
# при выполнении простых задач его эффективность нивелируется
#
#
#
