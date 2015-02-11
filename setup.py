#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import print_function

try:
    from setuptools import setup, find_packages
except ImportError as err:
    print(err)
    from distutils.core import setup

from codecs import open # To use a consistent encoding
from os import path
here = path.abspath(path.dirname(__file__))
# Get the long description from the relevant file
DEPENDENCIES = ['pytest', 'docopt', 'pandas', 'tables', 'numpy',
                'scipy', 'wx']
PACKAGES = ['amolf',
            #’amolf.analysis',
            #’amolf.image',
            'amolf.ixo',
            #’amolf.physics',
            #’amolf.simulations',
            'amolf.tools']
MODULES = ['amolf.ixo.get_file',
           'amolf.ixo.get_dir',
           ]

setup(
name='amolf',
# Versions should comply with PEP440. For a discussion on single-sourcing
# the version across setup.py and the project code, see
# http://packaging.python.org/en/latest/tutorial.html#version
version='0.1',
description='Python package for AMOLF research',
long_description='Collection of libraries, scripts and algorithms written in Python to aid the research and data analysis in AMOLF.',
# The project's main homepage.
url='https://github.com/Repythory/Libraries',
# Author details
author='The AMOLF Python Team',
author_email='',
# Choose your license
license='MIT',
# See https://pypi.python.org/pypi?%3Aaction=list_classifiers
classifiers=[
# How mature is this project? Common values are
# 3 - Alpha
# 4 - Beta
# 5 - Production/Stable
'Development Status :: 3 - Alpha',
# Indicate who your project is intended for
'Intended Audience :: Science/Research',
'Topic :: Software Development :: Build Tools',
# Pick your license as you wish (should match "license" above)
'License :: OSI Approved :: MIT License',
# Specify the Python versions you support here. In particular, ensure
# that you indicate whether you support Python 2, Python 3 or both.
'Programming Language :: Python',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Natural Language :: English',
'Operating System :: OS Independent',
'Topic :: Scientific/Engineering',
],
# What does your project relate to?
keywords='AMOLF',
# You can just specify the packages manually here if your project is
# simple. Or you can use find_packages().
packages=PACKAGES,
# List run-time dependencies here. These will be installed by pip when your
# project is installed. For an analysis of "install_requires" vs pip's
# requirements files see:
# https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
install_requires=DEPENDENCIES,
# List additional groups of dependencies here (e.g. development dependencies).
# You can install these using the following syntax, for example:
# $ pip install -e .[dev,test]
extras_require = {
'dev': ['check-manifest'],
'test': ['coverage'],
},
# If there are data files included in your packages that need to be
# installed, specify them here. If using Python 2.6 or less, then these
# have to be included in MANIFEST.in as well.
package_data={

},
# Although 'package_data' is the preferred approach, in some case you may
# need to place data files outside of your packages.
# see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
data_files=[],
# To provide executable scripts, use entry points in preference to the
# "scripts" keyword. Entry points provide cross-platform support and allow
# pip to create the appropriate form of executable for the target platform.
entry_points={
},
)
