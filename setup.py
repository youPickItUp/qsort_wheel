from os import system
from setuptools import setup, Distribution, Extension

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

my_extension = Extension('my_qsort', ['my_qsort/my_qsort.c'])

setup(
    name='my_qsort',
    version='0.1',
    packages=['my_qsort'],
    ext_package='my_qsort',
    ext_modules=[my_extension],
    distclass=BinaryDistribution
)

