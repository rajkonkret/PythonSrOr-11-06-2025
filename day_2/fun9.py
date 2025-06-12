import operator
import sys
import time
import tracemalloc
from functools import partial

import numpy as np

#  pip install numpy
# tracemalloc.start()
array1 = np.arange(10_000_000, dtype=np.int8)
array2 = np.arange(10_000_000, dtype=np.int8)
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
#
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# print(array1.dtype)
# print(np.iinfo(array1.dtype))
# # Current memory usage: 152.58807373046875 MB
# # Peak memory usage: 152.58807373046875 MB
# # int8
# # Machine parameters for int8
# # ---------------------------------------------------------------
# # min = -128
# # max = 127
# # ---------------------------------------------------------------
#
# # tracemalloc.start()
lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))


# # current, peak = tracemalloc.get_traced_memory()
# # tracemalloc.stop()
# #
# # print(f"Current memory usage: {current / 1024 ** 2} MB")
# # print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# # # Current memory usage: 762.9238739013672 MB
# # # Peak memory usage: 762.9239807128906 MB
#
# print(sys.int_info)
# # sys.int_info(bits_per_digit=30,
# #              sizeof_digit=4,
# #              default_max_str_digits=4300,
# #              str_digits_check_threshold=640)

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_time():
    time.sleep(2)


@measure_time
def my_for():
    l = []
    for x in lista1:
        l.append(x * 2)


@measure_time
def my_for_with_map():
    l_map = []
    l_map = list(map(lambda x: x * 2, lista2))


@measure_time
def my_for_list_compr():
    l = [i * 2 for i in lista2]


@measure_time
def my_for_map_operator():
    l_map = list(map(partial(operator.mul, 2), lista2))


my_time()
my_for()
my_for_with_map()
my_for_list_compr()
my_for_map_operator()
