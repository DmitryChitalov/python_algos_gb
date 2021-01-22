"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""

"""
Использование модуля cython помогает эффективно расходовать память.
"""

import run_python
import run_cython
import time
import memory_profiler

number = 100000


t1 = time.time()
m1 = memory_profiler.memory_usage()
run_python.test(number)
t2 =  time.time()
m2 = memory_profiler.memory_usage()

py_time = t2 - t1
py_memory = m2[0] - m1[0]
print("Python time = {}".format(py_time))
print("Python memory = {}".format(py_memory))

t1 = time.time()
m1 = memory_profiler.memory_usage()
run_cython.test(number)
t2 =  time.time()
m2 = memory_profiler.memory_usage()

cy_time = t2 - t1
cy_memory = m2[0] - m1[0]

print("Cython time = {}".format(cy_time))
print("Cython memory = {}".format(cy_memory))

"""
Python time = 16.026481866836548
Python memory = 0.1796875
Cython time = 0.1006467342376709
Cython memory = 0.0

Результаты показали, что использование cython не только эффективно расходует память, но и ускоряет на много время выполнения программы .
"""