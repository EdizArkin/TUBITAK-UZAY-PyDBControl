from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os



#
NAME = 'PyDBControl' 

VERSION = '0.1' 


AUTHOR = 'Ediz Arkin' 


AUTHOR_EMAIL = 'mail@example.com' 


DESCRIPTION = 'Veritabanı için işlevsel ve performans odaklı bir API'


URL = 'https://github.com/EdizArkin/TUBITAK-UZAY-PyDBControl' 


try:
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = 'Veritabanı için işlevsel ve performans odaklı bir API. Detaylı bilgi için lütfen projenin README.md dosyasını kontrol edin.'


LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'


INSTALL_REQUIRES = [
    'psycopg2-binary', 
    'cython',           
   
]


PYTHON_REQUIRES = '>=3.7'



CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7', 
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Operating System :: OS Independent', 
   
]

olu.
CYTHON_EXTENSIONS = [
    Extension(
        "PyDBControl.comparator", # 'my_db_api' paketinizin içindeki 'comparator' modülü
        sources=["PyDBControl/comparator.pyx"], # Kendi projenizdeki .pyx dosyasının yolu
     
       
    ),
    Extension(
        "my_db_api.table_manager", # 'my_db_api' paketinizin içindeki 'table_manager' modülü
        sources=["PyDBControl/table_manager.pyx"], # Kendi projenizdeki .pyx dosyasının yolu
       
    ),
   
]


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    url=URL,
   
    packages=find_packages(), 
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
    classifiers=CLASSIFIERS,
   
    ext_modules=cythonize(CYTHON_EXTENSIONS, compiler_directives={'language_level': "3"}),
    
    
    zip_safe=False, 
)
#sanal ortam aktif edilmeli sonra da pip install Cython ile yüklenmeli