from arv_int import *
from random import shuffle

num = [[[22,30],[27,32]],
        [[15,24],[24,31]],
        [[20,20],[35,35]],
        [[5,23],[24.5,40]],
        [[30,15],[50,25]],
        [[25,28],[40,40]],
        [[40,40],[45,60]]]
#print(len(num))
#print(num[0][0])
shuffle(num)
print num
print('\n\n')
#num = shuffle(num)
#num1 = shuffle(num1)
#print (shuffle(num), shuffle(num1))
#nums = [num, num1]
raiz = arv_int(num)
print raiz
print(consulta(raiz,22,58))
#del num
