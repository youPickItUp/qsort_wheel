from setuptools import setup, Distribution
from setuptools.command.install import install as SetupToolsInstall
from os import system

class MyInstall(SetupToolsInstall):
    def run(self):
        system('make libmy_qsort.so')
        SetupToolsInstall.run(self)

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setup(
    name='my_qsort',
    version='0.1',
    packages=['my_qsort'],
    package_data={
        'my_qsort': ['libmy_qsort.so']
    },
    cmdclass={'install': MyInstall},
    distclass=BinaryDistribution
)

