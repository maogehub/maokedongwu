#!/usr/bin/python
import ctypes
lib=ctypes.cdll.LoadLibrary("add.so")
print lib.add(10,15)
