#!/usr/bin/env python
import os
import io
import sys
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


readme = open('README.md').read()

requirements = []

setup(
    # Metadata
    name='Babieca',
    version='0.1.0',
    author='Babieca Team',
    author_email='3307370+babieca@users.noreply.github.com',
    url='https://github.com/babieca/stock_market',
    description='Super Simple Stock Market',
    long_description=readme,
    license='Apache Version 2.0',

    # Package info
    packages=find_packages(exclude=('tests',)),

    zip_safe=True,
    install_requires=requirements,
)
