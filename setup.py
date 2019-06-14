from os import system
from setuptools import setup, Distribution, Extension
from setuptools.command.build_ext import build_ext


class build_ext(build_ext):

    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypes)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if isinstance(ext, CTypes):
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if ext_name == 'my_qsort':
            return ext_name + '.so'
        return super().get_ext_filename(ext_name)

class CTypes(Extension): pass

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

my_extension = CTypes('my_qsort', sources = ['my_qsort/my_qsort.c'])

setup(
    name='my_qsort',
    version='0.1',
    packages=['my_qsort'],
    ext_package='my_qsort',
    ext_modules=[my_extension],
    cmdclass={'build_ext': build_ext},
    distclass=BinaryDistribution
)

