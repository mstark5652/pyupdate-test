#!/usr/bin/env python


#
# Created by mstark on July 5, 2019
#
# Copyright 2019 Michael Stark. All Rights Reserved.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

import sys, os

from config import VERSION

__version__ = VERSION

long_description = ''
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyupdatetest',
    version=__version__,
    author='Michael Stark',
    author_email='mstark5652@gmail.com',
    description='Test module for automatic software updater.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mstark5652/pyupdate-test',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Unix',
    ],
    install_requires=['setuptools >= 0.7.0'],
    packages=setuptools.find_packages(),
    zip_safe=True,
)

