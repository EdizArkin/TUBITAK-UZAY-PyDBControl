from setuptools import setup, find_packages
from Cython.Build import cythonize
from setuptools.extension import Extension

extensions = [
    Extension("mylib.tablemanager", ["mylib/tablemanager.pyx"]),
]

setup(
    name="mylib",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
    install_requires=[
        "psycopg2-binary",
        "python-dotenv",
        "cython"
    ],
    python_requires=">=3.7",
    author="Senin İsmin",
    description="Generic veritabanı API kütüphanesi",
)




