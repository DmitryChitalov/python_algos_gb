"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""


from memory_profiler import profile, memory_usage

##классика рекурсии
@profile
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



n = 22
m1 = memory_usage()
factorial(n)
m2 = memory_usage()
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {mem_diff} Mib")

##Выполнение заняло 0.3828125 Mib
"""Применение @profile запускает замеры столько раз, какова глубина рекурсии. 
без @profile памяти тратится меньше """



"""
 PyCharm 2020.2.3 (Community Edition)
Build #PC-202.7660.27, built on October 6, 2020
Runtime version: 11.0.8+10-b944.34 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: ParNew, ConcurrentMarkSweep
Memory: 1969M
Cores: 8
Non-Bundled Plugins: mobi.hsz.idea.gitignore
"""