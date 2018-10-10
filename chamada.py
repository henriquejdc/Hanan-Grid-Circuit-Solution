import os
import sys
a = '/usr/bin/time --verbose -o time.txt python2 teste.py case2.txt'
pipe = os.popen(a,'r')
d =  pipe.read()
pipe.close()
print d
