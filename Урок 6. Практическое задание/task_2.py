"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""


    # В целом, помимо тех способов, что Вы показали на уроке, я наткнулся на следующие советы и способы для оптимизации памяти:

# 1: Многопроцессорная обработка (для больших объемов памяти):

import multiprocessing

some_func(d):
computationsdata = [1,2,..,10000]
large datapool = multiprocessing.Pool(processes=number_of_processors)r = pool.map(some_func, data)
pool.close()

# 2. Многие советуют пользоваться Cython или, например, PyPy:

cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y

# 3. Пользоваться datafram'ами pandas вместо стандартных словарей питона (и/или вместо R даже) + ускорить pandas через dask:

import pandas as pd
import dask.dataframe as dd
from dask.multiprocessing import getdata = pd.DataFrame(…) #large data set

def my_time_consuming_function(d): # долго выполняемая функция d
data = dd.from_pandas(data, npartitions=30)def apply_my_func(df):
return df.apply(
(lambda row: my_time_consuming_function(*row)), axis=1)
def dask_apply():
return ddata.map_partitions(apply_my_func).compute(get=get)


# + куча всего по мелочи, вроде написания чистого кода без дублирующих переменных; генераторов, вместо функций (где можно); избегания циклов (особенно бесконечных) и т.д.