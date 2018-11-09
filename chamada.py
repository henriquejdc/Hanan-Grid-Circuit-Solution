import os
import sys
number_test = 10
for x in range(number_test):
    chamada = '/usr/bin/time --verbose -o times/time' + str(x) + '.txt pypy main.py cases/case' + str(x) + '.txt out/out' + str(x)
    os.system(chamada)
