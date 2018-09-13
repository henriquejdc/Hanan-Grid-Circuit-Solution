num = [3,1,2,2,3 ,3]
num1 = min(num)
print num1
print 4%2
test = []
prim = []
for numerados in range(3):
    list1 = []
    prim.append(list1)
for numerados in range(3):
    print "aqui"
    
prim[0].append(2)
prim[0].append(1)
prim[0].append(2)

prim[1].append(2)
prim[1].append(1)
prim[1].append(3)

if(prim[0][2]>prim[1][2]):
    prim[2].append("x"+str(prim[1][0]+prim[0][0]))
if(prim[0][2]<prim[1][2]):
    print "aqui porra"
    prim[2].append("y"+str(prim[1][2]+prim[0][2]))
    print prim[2]
if(prim[0][2]==prim[1][2]):
    prim[2].append("xy"+str(prim[1][0]+prim[0][0]))


if "y5" in prim[2]:
    print("ESSA MERDA")

testando = [1,2,3,4,5,6,7,8,9]
print testando
del testando[0]
print testando
