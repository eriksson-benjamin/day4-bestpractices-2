#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:18:12 2021

@author: beriksso
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
      ext_modules = cythonize('fastloop.pyx')
      )
