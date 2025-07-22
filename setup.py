from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

extensions = [
    Extension("tablemanager", ["tablemanager.pyx"]),
]

setup(
    name="my_cython_project",
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
)
