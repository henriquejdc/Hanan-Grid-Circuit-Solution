import os
import sys
number_test = 2
for x in range(number_test):
    chamada = '/usr/bin/time --verbose -o times/time' + str(x) + '.txt python2 teste.py cases/case' + str(x) + '.txt'
    os.system(chamada)
