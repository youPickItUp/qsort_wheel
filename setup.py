from setuptools import setup, Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setup(
    name="my_qsort",
    version="0.1",
    packages=["my_qsort"],
    package_data={
        "my_qsort": ['libmy_qsort.so']
    },
    distclass=BinaryDistribution
)

