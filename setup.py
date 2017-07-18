###############################################################################
# -*- coding: utf-8 -*-
# cgparam: Parameterization of a coarse-grained model with Stillinger-Weber 
#          potentials.
#
# Authors: Pu Du
# 
# Released under the GNU License
###############################################################################

from setuptools import setup, find_packages
import cgparam
import os

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='cgparam',
    version='0.0.1',
    description='Parameterization of a coarse-grained model with Stillinger-Weber potentials',
    long_description=readme(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords=['coarse-grained model', 'Stillinger-Weber potentials'],
    author='Pu Du',
    author_email='pudugg@gmail.com',
    maintainer='Pu Du',
    maintainer_email='pudugg@gmail.com',
    url='https://github.com/ipudu/cgparam',
    license='GNU',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cgparam = cgparam.cgparam:command_line_runner',
        ]
    },
    install_requires=[
        'numpy',
        'six',
        'progress',
        'scipy',
        'matplotlib',
    ],
)