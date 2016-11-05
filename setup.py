#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='migraperf',
    version='1.0',
    description='Performance test of django migrations',
    long_description='',
    author='Nicolas Lara',
    author_email='nicolas@lincolnloop.com',
    url='https://github.com/nicolaslara/migraperf/',
    packages=find_packages(),
    scripts=[
        'manage.py'
    ],
    package_data={
        'pp': ['templates/*.*'],
        'docs': ['*'],
        'client': ['*'],
    },
    include_package_data=True,
    install_requires=[
        # TODO: Do we want to move the requirements.txt here? People would
        #       need to install packages using `python setup.py develop`.
    ],
)