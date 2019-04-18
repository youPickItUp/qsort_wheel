import os
from sys import platform
from ctypes import *

extension = 'so' if platform == "linux" or platform == "linux2" else 'dll'
lib_path = os.path.join(os.path.dirname(__file__), 'libmy_qsort.' + extension)
my_qsort = CDLL(lib_path)

def my_sort(arr, compare):
    # create C type array
    IntArray = c_int * len(arr)
    c_arr = IntArray(*arr)

    # create C type compare
    CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
    c_compare = CMPFUNC(lambda x, y: compare(x[0], y[0]))

    my_qsort.my_qsort(c_arr, len(c_arr), sizeof(c_int), c_compare)

    arr.clear()
    arr.extend(list(c_arr))

def hello():
    print("Hello, World!")

