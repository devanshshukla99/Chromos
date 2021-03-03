
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'Chromos',
    version = '2.2',
    scripts=['src/Chromos/Chromos.py'],
    setup_requires = ['pytest-runner',],
    tests_require = ['pytest',],
    author = "devanshshukla99",
    description = "Package for getting colored text output in Python terminal",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/devanshshukla99/Chromos",
    license = "MIT LICENCE",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )

# python3 setup.py bdist_wheel
