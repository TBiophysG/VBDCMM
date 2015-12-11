# python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize("c_dcmm4vb_func.pyx"),
    include_dirs = [numpy.get_include()]
)
