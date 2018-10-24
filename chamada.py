import os
import sys
number_test = 3
for x in range(number_test):
    chamada = '/usr/bin/time --verbose -o times_m/time' + str(x) + '.txt python2 main.py cases/cases_m/case' + str(x) + '.txt'
    chamada = '/usr/bin/time --verbose -o times_o/time' + str(x) + '.txt python2 main.py cases/cases_o/case' + str(x) + '.txt'
    chamada = '/usr/bin/time --verbose -o times_c/time' + str(x) + '.txt python2 main.py cases/cases_c/case' + str(x) + '.txt'
    os.system(chamada)
