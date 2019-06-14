import os
from distutils.sysconfig import get_config_var
from sys import platform
from ctypes import *

lib_name = 'my_qsort.so'
lib_path = os.path.join(os.path.dirname(__file__), lib_name)
my_qsort = CDLL(lib_path)

def my_sort(arr, compare):
    # create C type array
    IntArray = c_int * len(arr)
    c_arr = IntArray(*arr)

    # create C type compare
    CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
    c_compare = CMPFUNC(lambda x, y: compare(x[0], y[0]))

    my_qsort.my_qsort(c_arr, len(c_arr), sizeof(c_int), c_compare)

    del arr[:]
    arr.extend(list(c_arr))

def hello():
    print("Hello, World!")

