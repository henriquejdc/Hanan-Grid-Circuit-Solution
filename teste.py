from arv_int import *
from random import shuffle

num = [[22,30],[15,24],[20,20],[5,23],[30,15],[25,28],[40,40]]
num1 = [[27,32],[24,31],[35,35],[24.5,40],[50,25],[40,40],[45,60]]
shuffle(num)
shuffle(num1)
print num
print num1
print('\n\n')
#num = shuffle(num)
#num1 = shuffle(num1)
#print (shuffle(num), shuffle(num1))
nums = [num, num1]
raiz = arv_int(nums)
print raiz
print(consulta(raiz,22,58))
#del num
