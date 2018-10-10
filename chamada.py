import os
import sys
a = '/usr/bin/time --verbose -o times/time.txt python2 teste.py cases/case2.txt'
b = '/usr/bin/time --verbose -o times/time1.txt python2 teste.py cases/case2.txt'
os.system(a)
os.system(b)
