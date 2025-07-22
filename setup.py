from setuptools import setup, find_packages

setup(
    name="pydbcontrol",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "psycopg2",
    ],
    author="Ediz Arkin",  # geliştirici adi
    author_email="",  # maili
    description="Veritabanı için işlevsel bir API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/EdizArkin/TUBITAK-UZAY-PyDBControl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
