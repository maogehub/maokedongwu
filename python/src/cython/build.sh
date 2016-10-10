#!/bin/bash

#build binary
cython --embed speed_test.pyx -o speed_test.c
gcc -I /usr/include/python2.7 speed_test.c -lpython2.7 -o speed_test

#build so
cython speed_test.pyx
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I/usr/include/python2.7/ -lpython2.7 -o speed_test.so speed_test.c
