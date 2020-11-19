# -*- coding: utf-8 -*-
"""
Created on 2020/7/20

@author: curya
"""
from __future__ import absolute_import, print_function

import os
import sys

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

# For demo purposes, we build our own tiny library.
try:
    print("building libvibe-background-sequential.a")
    # 将C代码编译为.o目标文件
    # assert os.system("gcc -shared -fPIC -c vibe-background-sequential.c -o vibe-background-sequential.o") == 0
    # assert os.system("gcc -std=c99 -O3 -Wall -Werror -pedantic -Wno-unused-function -Wno-unused-parameter -Wno-deprecated -Wno-deprecated-declarations -Wno-sign-compare -Wno-unused-but-set-parameter -shared -fPIC -c vibe-background-sequential.c  -o vibe-background-sequential.o") == 0
    assert os.system("gcc -std=c99 -O3 -Wall -Werror -pedantic -Wno-unused-function -Wno-unused-parameter -Wno-deprecated -Wno-deprecated-declarations -Wno-sign-compare -fPIC -c vibe-background-sequential.c  -o vibe-background-sequential.o") == 0
    
    # 将.o目标文件编译为.a静态库文件
    assert os.system("ar rcs libvibe-background-sequential.a vibe-background-sequential.o") == 0
    print('built libvibe-background-sequential.a')
except:
    if not os.path.exists("libvibe-background-sequential.a"):
        print("Error building external library, please create libmymath.a manually.")
        sys.exit(1)

# Here is how to use the library built above.
ext_modules = cythonize([
    Extension("py_vibe",
              sources=["py_vibe.pyx"],
              include_dirs=[os.getcwd(), np.get_include()],  # path to .h file(s), np.get_include(): avoid fatal error: numpy/arrayobject.h: No such file or directory”
              library_dirs=[os.getcwd()],  # path to .a or .so file(s)
              libraries=['vibe-background-sequential'])  # 静态库文件libvibe-background-sequential.a的名称
], annotate=True)

setup(
    name='Demos',
    ext_modules=ext_modules,
)