from setuptools import setup, find_packages

setup(
    name="mylib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "psycopg2-binary",
        "python-dotenv",
        "pandas",
    ],
    python_requires=">=3.7",
    author="Senin İsmin",
    description="Generic veritabanı API kütüphanesi",
)

