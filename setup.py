from setuptools import setup, find_packages

setup(
    name="pydbcontrol",
    version="0.1.0",
    packages=["pydbcontrol"],
    install_requires=[
        'psycopg2-binary',
        'pandas',
        'python-dotenv'
    ],
    author="Ediz Arkin Kobak",
    author_email="arkinediz@gmail.com",
    description="A Python library to control and compare PostgreSQL tables",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/EdizArkin/TUBITAK-UZAY-PyDBControl",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)