from arv_int import *
import random

num = [[22,30],[15,24],[20,20],[5,23],[30,15],[25,28],[40,40]]
num1 = [[27,32],[24,31],[35,35],[24.5,40],[50,25],[40,40],[45,60]]
#num = random.shuffle(num)
#num1 = random.shuffle(num1)
print (num, num1)
nums = [num, num1]

#print (nums)
raiz = arv_int(nums)
print (raiz)

#del num
